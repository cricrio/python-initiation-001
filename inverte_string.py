# - Écrire une fonction Python qui prend en entrée un tableau de chaînes de caractères et renvoie un nouveau tableau avec les chaînes de caractères inversées.
#  Par exemple, si le tableau d'entrée est ['hello', 'world'], la fonction devrait renvoyer ['olleh', 'dlrow'].


def invert_array(array):
    inverted_array = []
    for word in array:
        inverted_word = word[::-1]
        inverted_array.append(inverted_word)
    return inverted_array


def invert(string):
    return string[::-1]


def invert_with_comprehension(array):
    l = [w[::-1] for w in array]
    return l


chaine = ["hello", "world"]

print(invert_with_comprehension(chaine))
