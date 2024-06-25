# Strings

chaine = "Bonjour"
print(chaine.upper(), chaine.lower())
print(
    chaine.center(50, " "),
)


# Type convertion

number = int("123")
print(number, type(number))

b1 = bool(1)

print(b1, type(b1))

b2 = bool(0)

b3 = bool("")

b4 = bool([])

print(b2, b3, b4)
