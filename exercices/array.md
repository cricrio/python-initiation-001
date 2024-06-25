## List

### Exo 1

- Créer une fonction qui prend en paramétre une list de nombres entiers  
  - qui retourne un nouveau tableau contenant tout les nombres pairs. Utiliser `x % 2` 
  - qui retourne la somme.
  - qui retourne la moyenne
  - qui retourne un tuple qui contient le plus grand nombre et le plus petit

- Créer une fonction qui prend en paramétre une liste de tuples (notes, coefficient) et calcule la moyenne pondérée 

- Écrire une fonction Python qui prend en entrée un tableau d'entiers et renvoie un nouveau tableau avec les nombres uniques du tableau d'entrée, c'est-à-dire en supprimant les doublons.

- Créer une fonction Python qui prend en entrée une liste et renvoie le tableau d'entrée inversé.


### Exo 2


- Écrire une fonction Python qui prend en entrée un tableau de chaînes de caractères et renvoie un nouveau tableau avec les chaînes de caractères inversées. Par exemple, si le tableau d'entrée est ['hello', 'world'], la fonction devrait renvoyer ['olleh', 'dlrow']. 
 - for / slicing [:]
 - list comprehension (complexe deuxième partie de correction)



## String

### Compter les voyelles

Écrire une fonction Python qui prend en entrée une chaîne de caractères et renvoie le nombre de voyelles qu'elle contient.

```python
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Exemple d'utilisation de la fonction
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print(vowel_count)  # Output: 4
```

### Est-ce un palindrome ? 

Écrire une fonction Python qui prend en entrée une chaîne de caractères et renvoie True si la chaîne est un palindrome (se lit de la même manière de gauche à droite et de droite à gauche), sinon False.

```python 
def is_palindrome(input_string):
    # Convertir la chaîne en minuscules et supprimer les espaces
    input_string = input_string.lower().replace(" ", "")
    
    # Vérifier si la chaîne est égale à sa version inversée
    return input_string == input_string[::-1]

# Exemple d'utilisation de la fonction
input_string = "A man, a plan, a canal, Panama"
result = is_palindrome(input_string)
print(result)  # Output: True

```

### Mettre une lettre majuscule a chaque mots ?

Faire une fonction qui prend en paramètres une chaine de charactères et retourne la chaine avec chaque mots avec une majuscule.

## Dictionnary 

Exercice 1:
Écrire une fonction Python qui prend en entrée un dictionnaire de mots et de fréquences et renvoie le mot le plus fréquent.

Exercice 2:
Écrire une fonction Python qui prend en entrée deux dictionnaires et renvoie un nouveau dictionnaire contenant les clés communes aux deux dictionnaires avec la somme des valeurs correspondantes.

Exercice 3:
Écrire une fonction Python qui prend en entrée un dictionnaire de notes d'étudiants (nom en clé et note en valeur) et renvoie le nom de l'étudiant ayant obtenu la meilleure note.

Exercice 4:
Écrire une fonction Python qui prend en entrée un dictionnaire de listes d'entiers et renvoie un nouveau dictionnaire avec la moyenne de chaque liste.

=> Exercice 5: Faire une function qui prend en entrée une chaine de caractères et renvoie une dictionnaire contenant chaques lettres et leur fréquences d'apparition   
