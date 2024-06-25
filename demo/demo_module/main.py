from cli import ask
import random


def main():
    print(ask("Quel est votre prénom? ", "string"))
    # print(ask("Quel est votre nom? ", "string"))
    # print(ask("Quel est votre âge? ", "int"))
    # print(ask("Quel est votre taille? ", "float"))
    # print(ask("Quel est votre poids? ", "float"))

    print(random.uniform(1, 100))


main()
