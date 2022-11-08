

def viiva(size, character):
    if character == "":
        character = "*"
    print(character[0] * size)

def risulaatikko(height):
    i = 1
    while i <= height:
        viiva(10, "#")
        i += 1

if __name__ == "__main__":
    risulaatikko(5)