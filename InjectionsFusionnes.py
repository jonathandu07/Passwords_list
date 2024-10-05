import asyncio
import aiofiles
import aiomysql
import hashlib
import os
import re
from alive_progress import alive_bar

# Paramètres de l'environnement
input_directory = r"C:\Users\alpha\Documents\GitHub\Passwords_list\split_files"
mysql_host = 'localhost'
mysql_user = 'jonathan'
mysql_password = 'J0n@thandu07'
mysql_db = 'passwords_db'
mysql_table = 'passwords'
concurrency_limit = 100  # Nombre maximum de fichiers à traiter simultanément

# Définir le regex pour les mots de passe valides
password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\W)(?=.*\d.*\d)[A-Za-z\d\W]{16,32}$')

# Fonction pour hacher les mots de passe
def hash_passwords(password):
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    sha512_hash = hashlib.sha512(password.encode()).hexdigest()
    return sha256_hash, sha512_hash

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

# Fonction pour filtrer et insérer les mots de passe dans la base de données
async def process_single_file(file_path, connection, bar):
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as infile:
        async with connection.cursor() as cursor:
            async for line in infile:
                password = line.strip()
                # Filtrer les mots de passe valides selon le regex
                if password_regex.match(password):
                    sha256_hash, sha512_hash = hash_passwords(password)
                    # Insérer les mots de passe hachés dans la base de données
                    await cursor.execute(f'''
                        INSERT INTO {mysql_table} (password, sha256, sha512)
                        VALUES (%s, %s, %s)
                    ''', (password, sha256_hash, sha512_hash))

                bar()  # Mettre à jour la barre de progression

# Fonction principale pour le traitement des fichiers en parallèle
async def process_files():
    # Connexion à la base de données MySQL
    connection = await aiomysql.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        db=mysql_db
    )

    # Initialisation de la base de données
    await init_db(connection)

    # Créer une liste de tous les fichiers .txt
    txt_files = [os.path.join(input_directory, filename)
                 for filename in os.listdir(input_directory) if filename.endswith(".txt")]

    # Calculer le nombre total de lignes pour la barre de progression
    total_lines = 0
    for file in txt_files:
        async with aiofiles.open(file, 'r', encoding='utf-8') as f:
            total_lines += sum(1 for _ in await f.readlines())

    # Initialiser la barre de progression
    with alive_bar(total_lines, title="Processing passwords") as bar:
        # Utiliser un sémaphore pour limiter la concurrence
        semaphore = asyncio.Semaphore(concurrency_limit)

        async def process_with_semaphore(file_path):
            async with semaphore:
                await process_single_file(file_path, connection, bar)

        # Lancer le traitement de tous les fichiers en parallèle avec une limite
        await asyncio.gather(*(process_with_semaphore(file_path) for file_path in txt_files))

    # Sauvegarder les changements dans la base de données et fermer la connexion
    await connection.commit()
    connection.close()

    print(f"\nInsertion terminée ! Les mots de passe ont été ajoutés dans la base de données MySQL.")

# Exécuter la fonction principale
asyncio.run(process_files())
