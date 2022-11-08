

def viiva(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def kolmio(size):
    i = 1
    while i <= size:
        viiva(i, "#")
        i += 1

if __name__ == "__main__":
    kolmio(5)