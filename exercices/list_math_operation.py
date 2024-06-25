# - Créer une fonction qui prend en paramétre une list de nombres entiers
#   - qui retourne un nouveau tableau contenant tout les nombres pairs. Utiliser `x % 2`
#   - qui retourne la somme.
#   - qui retourne la moyenne
#   - qui retourne un tuple qui contient le plus grand nombre et le plus petit

array = [58, 52, 1058, 2, 12, 1, 2]


def get_even_numbers(lst):
    even_number = []
    for number in lst:
        if number % 2 == 0:
            even_number.append(number)
    return even_number


def sum_numbers(lst):
    sum = 0
    for number in lst:
        sum += number
    return sum


def average(lst):
    sum = sum_numbers(lst)
    return sum / len(lst)


print(average(list))


def get_min_max(lst):
    min = array[0]
    max = array[0]
    for number in lst:
        if min > number:
            min = number
        elif max < number:
            max = number
    return (min, max)


print(get_min_max(array))
