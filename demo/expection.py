import traceback


def demo_zero_division():
    try:
        print(15 / 0)
    except ZeroDivisionError:  # ou except:
        traceback.print_exc()  # Affiche le traceback dans la console
        print("You have done a division by 0.")
    print("After the division by 0.")


demo_zero_division()
