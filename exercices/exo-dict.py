# Écrire une fonction Python qui prend en entrée un dictionnaire de mots et de fréquences et renvoie le mot le plus fréquent.

words = {
    "maison": 25,
    "voiture": 32,
    "fournisseur": 54,
}


def get_most_frequent_word(words):
    most_frequent = {"word": "", "frequence": 0}

    for key, frequence in words.items():
        if frequence > most_frequent["frequence"]:
            most_frequent = {
                "word": key,
                "frequence": frequence,
            }
    return most_frequent.get("word")


print(get_most_frequent_word(words))
