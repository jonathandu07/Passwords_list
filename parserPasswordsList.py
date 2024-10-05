import os

input_file = r"C:\Users\alpha\Documents\GitHub\Passwords_list\mots2passes_unique.txt"
output_directory = r"C:\Users\alpha\Documents\GitHub\Passwords_list\split_files"
lines_per_file = 1000  # Nombre de lignes par fichier de sortie

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_directory, exist_ok=True)

def split_file():
    with open(input_file, 'r', encoding='utf-8') as infile:
        current_file_number = 1
        current_line_count = 0
        output_file = None

        for line in infile:
            # Créer un nouveau fichier si nécessaire
            if current_line_count % lines_per_file == 0:
                if output_file:
                    output_file.close()
                output_file_path = os.path.join(output_directory, f"mots2passes_part_{current_file_number}.txt")
                output_file = open(output_file_path, 'w', encoding='utf-8')
                current_file_number += 1

            # Écrire la ligne dans le fichier de sortie actuel
            output_file.write(line)
            current_line_count += 1

        # Fermer le dernier fichier de sortie ouvert
        if output_file:
            output_file.close()

    print(f"Le fichier a été découpé en {current_file_number - 1} parties dans le dossier : {output_directory}")

split_file()
