import asyncio
import aiofiles
import aiosqlite
import hashlib
import os
from alive_progress import alive_bar

input_directory = r"C:\Users\alpha\Documents\GitHub\Passwords_list\split_files"
db_file = r"C:\Users\alpha\Documents\GitHub\Passwords_list\passwords.db"
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

# Fonction pour initialiser la base de données
async def init_db():
    async with aiosqlite.connect(db_file) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT,
                sha256 TEXT,
                sha512 TEXT
            )
        ''')
        await db.commit()

# Fonction pour traiter un fichier unique
async def process_single_file(file_path, db, bar):
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as infile:
        async for line in infile:
            password = line.strip()
            sha256_hash, sha512_hash = hash_passwords(password)

            # Insérer le mot de passe et ses hachages dans la base de données
            await db.execute('''
                INSERT INTO passwords (password, sha256, sha512)
                VALUES (?, ?, ?)
            ''', (password, sha256_hash, sha512_hash))

            bar()  # Mettre à jour la barre de progression

# Fonction pour traiter les fichiers en parallèle avec une limite de concurrence
async def process_files():
    # Initialiser la base de données
    await init_db()
    total_lines = await count_total_lines(input_directory)

    async with aiosqlite.connect(db_file) as db:
        # Initialiser la barre de progression
        with alive_bar(total_lines, title="Processing passwords") as bar:
            # Créer une liste de tous les fichiers .txt
            txt_files = [os.path.join(input_directory, filename)
                         for filename in os.listdir(input_directory) if filename.endswith(".txt")]

            # Utiliser un sémaphore pour limiter la concurrence
            semaphore = asyncio.Semaphore(concurrency_limit)

            async def process_with_semaphore(file_path):
                async with semaphore:
                    await process_single_file(file_path, db, bar)

            # Lancer le traitement de tous les fichiers en parallèle avec une limite
            await asyncio.gather(*(process_with_semaphore(file_path) for file_path in txt_files))

        # Sauvegarder les changements dans la base de données
        await db.commit()

    print(f"\nInsertion terminée ! Les mots de passe ont été ajoutés dans la base de données : {db_file}")

# Exécuter la fonction principale
asyncio.run(process_files())
