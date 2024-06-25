# Array

array = ["foo", "bar", "baz", "qux", "quux", "corge"]

for item in array:
    print(item)

length = len(array)
for index in range(length):
    print(f"{index} {array[index]}")


array[2] = "Bonjour - 2"

bla = array.pop(1)
print(bla, array)

array.append("Hello")


array.insert(2, "World")

print(array)


array.extend([1, 2, 3, 4, 5])

print(array)


tuple = ("foo", "bar", "baz", "qu")


for item in tuple:
    print(item)

## Destructuring

(
    a,
    b,
    c,
    d,
) = tuple

print(
    a,
    b,
)


def add(a, b):
    return a + b


# Array slicing

array = ["foo", "bar", "baz", "qux", "quux", "corge"]

print("get by negative index", array[-5])


print("slicing by positive index ", array[1:3])

print("slicing by negative", array[-3:-1])


print("without first arg", array[:3])

print("without second arg", array[3:])

tab = array[:]

print("original", array)

tab[0] = "Hello"

print(array)

print("copy", array[:])

print("step 2", array[::2])

print("step -1", array[::-1])
