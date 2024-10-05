import asyncio
import aiofiles
from alive_progress import alive_bar

input_file = r"C:\Users\alpha\Documents\GitHub\Passwords_list\mots2passes.txt"
output_file = r"C:\Users\alpha\Documents\GitHub\Passwords_list\mots2passes_unique.txt"

async def count_lines(file_path):
    # Compter le nombre total de lignes dans le fichier
    count = 0
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
        async for _ in f:
            count += 1
    return count

async def remove_duplicates():
    # Utiliser un set pour stocker les lignes uniques
    unique_lines = set()

    # Compter les lignes pour la barre de progression
    total_lines = await count_lines(input_file)

    # Lire le fichier de manière asynchrone
    async with aiofiles.open(input_file, 'r', encoding='utf-8') as infile:
        # Initialiser la barre de progression
        with alive_bar(total_lines, title="Processing lines") as bar:
            async for line in infile:
                unique_lines.add(line.strip())  # Ajouter chaque ligne au set pour supprimer les doublons
                bar()  # Mettre à jour la barre de progression

    # Écrire les lignes uniques dans un nouveau fichier de manière asynchrone
    async with aiofiles.open(output_file, 'w', encoding='utf-8') as outfile:
        await outfile.write('\n'.join(unique_lines))

    print(f"\nTraitement terminé ! Les doublons ont été retirés et le fichier est enregistré sous : {output_file}")

# Exécuter la fonction asynchrone
asyncio.run(remove_duplicates())
