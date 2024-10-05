import asyncio
import aiofiles
import aiomysql
import hashlib
import os
from alive_progress import alive_bar

input_directory = r"C:\Users\alpha\Documents\GitHub\Passwords_list\split_files"
mysql_host = 'localhost'  # Adresse du serveur MySQL
mysql_user = 'jonathan'  # Nom d'utilisateur MySQL
mysql_password = 'J0n@thandu07'  # Mot de passe MySQL
mysql_db = 'passwords_db'  # Nom de la base de données
mysql_table = 'passwords'  # Nom de la table dans la base de données
concurrency_limit = 100  # Nombre maximum de fichiers à traiter simultanément

# Fonction pour hacher les mots de passe
def hash_passwords(password):
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    sha512_hash = hashlib.sha512(password.encode()).hexdigest()
    return sha256_hash, sha512_hash

# Fonction pour compter toutes les lignes de tous les fichiers pour la barre de chargement
async def count_total_lines(directory):
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                async for _ in f:
                    count += 1
    return count

# Fonction pour initialiser la table dans la base de données MySQL
async def init_db(connection):
    async with connection.cursor() as cursor:
        await cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {mysql_table} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                password TEXT,
                sha256 VARCHAR(64),
                sha512 VARCHAR(128)
            )
        ''')
        await connection.commit()

# Fonction pour traiter un fichier unique
async def process_single_file(file_path, connection, bar):
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as infile:
        async with connection.cursor() as cursor:
            async for line in infile:
                password = line.strip()
                sha256_hash, sha512_hash = hash_passwords(password)

                # Insérer le mot de passe et ses hachages dans la base de données
                await cursor.execute(f'''
                    INSERT INTO {mysql_table} (password, sha256, sha512)
                    VALUES (%s, %s, %s)
                ''', (password, sha256_hash, sha512_hash))

                bar()  # Mettre à jour la barre de progression

# Fonction pour traiter les fichiers en parallèle avec une limite de concurrence
async def process_files():
    # Connexion à la base de données MySQL
    connection = await aiomysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        db=mysql_db
    )

    await init_db(connection)

    total_lines = await count_total_lines(input_directory)

    # Initialiser la barre de progression
    with alive_bar(total_lines, title="Processing passwords") as bar:
        # Créer une liste de tous les fichiers .txt
        txt_files = [os.path.join(input_directory, filename)
                     for filename in os.listdir(input_directory) if filename.endswith(".txt")]

        # Utiliser un sémaphore pour limiter la concurrence
        semaphore = asyncio.Semaphore(concurrency_limit)

        async def process_with_semaphore(file_path):
            async with semaphore:
                await process_single_file(file_path, connection, bar)

        # Lancer le traitement de tous les fichiers en parallèle avec une limite
        await asyncio.gather(*(process_with_semaphore(file_path) for file_path in txt_files))

    # Sauvegarder les changements dans la base de données
    await connection.commit()
    connection.close()

    print(f"\nInsertion terminée ! Les mots de passe ont été ajoutés dans la base de données MySQL.")

# Exécuter la fonction principale
asyncio.run(process_files())
