def joulukuusi(height):
    print("joulukuusi!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")

if __name__ == "__main__":
    joulukuusi(5)