pizzas = [
    (0, "Regina", 12),
    (1, "Chèvre miel", 11),
    (2, "Savoyrde", 12),
    (3, "Reine", 15),
    (4, "Ananas", 17),
]

user_selection = [
    0,
    0,
    0,
    0,
    0,
]
done = False

while done == False:
    for id, name, price in pizzas:
        print(f"{id} {name}: {price}")
    selection = input("Enter the number of the product you want to buy: ")
    pizza_index = int(
        selection
    )  ## The function input returns a string, so we need to convert it to an integer.
    if pizza_index < 0:
        done = True
    else:
        user_selection[pizza_index] = user_selection[pizza_index] + 1


orders = []
total = 0
for index in range(len(user_selection)):
    if user_selection[index]:
        s = user_selection[index]
        orders.append(f"{names[index]} x {s} ")
        total += s * prices[index]  # total = total + s * prices[index]

print(orders)
print(f"Total: {total}")
