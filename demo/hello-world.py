string = "Hello World"
string2 = "Hello World"
string3 = """Hello World
Coucou ! 


"""

print("Hello World")
# name = input("What is your name?")

## ** is a equivalent of pow() and used only numbers
print(2**3)  # result: 8

print(7 / 3)
print(7 // 3)

print("bob" in "Hello World")
print("Hello" in "Hello World")
# La division entière retourne un ceil ou un floor ??

# Falsy values: "", 0, False, None, [], {}


# value = 15

# if value > 10:
#     print("The value is greater than 10")
# if value < 10:
#     print("The value is less than 10")
# if value > 11 and value < 17:
#     print("The value is greater than 11 and less than 17")
# else:
#     print("The value is not greater than 10")

name = "DD"
last = "AAA"
print(f"Hello World, {name} {last}")


# Typings

var: str = "Hello World"
n: int = 15

# Numbres longs

n1: int = 1_000


tableau = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
]

print(tableau[0])
print(tableau[-2])

array = range(0, 10)
for item in array:
    print(item)

print(len(array))

print(array)
