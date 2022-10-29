def shakkilauta(length):
    num = ["0", "1"]

    for x in range(length):
        for y in range(length):
            i = num[(x + y + 1) % 2]
            print(i, end=(''))
        print()
    

# Testing the function
if __name__ == "__main__":
    shakkilauta(3)