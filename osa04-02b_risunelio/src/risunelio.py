def viiva(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def risunelio(size):
    i = 1
    while i <= size:
        viiva(size, "#")
        i += 1

if __name__ == "__main__":
    risunelio(5)