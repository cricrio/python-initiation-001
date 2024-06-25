def ask(question, type):
    if type == "int":
        return int(input(question))
    elif type == "float":
        return float(input(question))
    return input(question)
