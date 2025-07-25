authors = ["Virginia Woolf", "JohnSteinbeck", "Domingo Dave"]

def add_comma(name):
    parts = name.split(" ")

    return parts[1] + ", " + parts[0]


authors_update = [add_comma(name) for name in authors]
print(authors_update)