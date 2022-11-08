def viiva(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

if __name__ == "__main__":
    viiva(5, "x")