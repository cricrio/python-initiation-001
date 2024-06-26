# Step 1: ouvrir le fichier with open(path,  mode) as file (mode 'r' ou 'w')
# Step 2: utiliser les file.read() ou file.readline() pour la lecture et file.write() ou file.writelines(['tet','etetet'])
# Pas besoin de fermer le fichier avec de la synctax with


def manual_open():
    try:
        file = open("demo.txt")
        data = file.read()
        print(data)
    except FileNotFoundError:
        print("the file is not found")
    finally:
        file.close()


## Auto closing of the file when extiting the with block
def recommended_open_to_read():
    try:
        with open("demo.txt", "r") as file:
            data = file.read()
            print(data)
        print("the file is closed")
    except FileNotFoundError:
        print("File not found")


def write():
    try:
        with open("demo.txt", "w") as file:
            file.write("Bye, bye")
    except FileNotFoundError:
        print("File not found")


## Function not working we cannot open a file to read and write
## If you want to read and write a file in the program you must open it twice.
def read_write():
    try:
        with open("demo.txt", "r+w") as file:
            file.write("Bye, bye")
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("File not found")


def read_by_line():
    try:
        with open("demo.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print("File not found")


def write_at_end_():
    try:
        with open("demo.txt", "r+w") as file:
            file.write("Bye, bye")
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("File not found")


write()
