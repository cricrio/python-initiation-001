# - Un utilisateur rentre du texte ligne par ligne.
#     - On enregistre ligne dans un fichier.
#     - boucle while et pour quitter l'utilisteur va 'q'

#   - On lit le fichier et on affiche son contenu.
from os import path


def main():
    done = False
    script_dir = path.dirname(__file__)
    file_path = path.join(script_dir, "./data/user_file.txt")

    try:
        user_entries = []
        while not done:
            text = input("Saiser votre text: ")
            if text == "q":
                done = True
            else:
                user_entries.append(f"{text}\n")
        with open(file_path, "w") as writer:
            writer.writelines(user_entries)
        with open(file_path, "r") as reader:
            data = reader.read()
            print(data)
    except FileNotFoundError:
        print("file not found")


main()
