def transform_name(first, last):
    return f"{first} {last.upper()}"


def get_user():
    first = input("What is your first name?")
    last = input("What is your last name?")
    return (first, last)


def welcome_user(first, last):
    print(transform_name(first, last))


def ask(question, answers):
    while True:
        selection = input(f"{question} answer: {answers} ")
        if selection in answers:
            return selection
        print("Your answer is not reconized")


# def get_book_in_stocks(books):
#     in_stocks = []
#     for book in books:
#         if book["stock"]:
#             in_stocks.append(book)
#     return in_stocks


def get_book_in_stocks(books):
    return [book for book in books if book["stock"]]


def display_books(books):
    for book in books:
        print(f"Id: {book['id']}, title: {book['title']}]")


def update_books(book_id, books, action):
    for book in books:
        if book["id"] == book_id:
            if action == "out":
                book["stock"] = book["stock"] - 1
            else:
                book["stock"] = book["stock"] + 1
            break


def get_book_selection(books):
    while True:
        books_in_stocks = get_book_in_stocks(books)
        display_books(books_in_stocks)
        answer_to_selection = [book["id"] for book in books_in_stocks]
        answer_to_selection.append("Q")
        book_id = ask("What book do you want", answer_to_selection)
        if book_id == "Q":
            break
        update_books(book_id, books, "out")


def librairian_actions(books):
    pass


def user_actions(books):
    first, last = get_user()
    welcome_user(first, last)
    get_book_selection(books)
    print(books)


def main():
    books = [
        {"id": "0", "title": "Harry Potter", "stock": 5},
        {"id": "1", "title": "Harry Potter 2", "stock": 5},
        {"id": "2", "title": "Harry Potter 3", "stock": 5},
        {"id": "3", "title": "Harry Potter 4", "stock": 0},
    ]
    users_with_books = {}

    selection = ask("What is your status", ["L", "U"])
    if selection == "L":
        librairian_actions(books, users_with_books)
    elif selection == "U":
        user_actions(books)


main()
