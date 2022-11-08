def viiva(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def nelio(size, character):
    i = 1
    while i <= size:
        viiva(size, character)
        i += 1

if __name__ == "__main__":
    nelio(5, "x")