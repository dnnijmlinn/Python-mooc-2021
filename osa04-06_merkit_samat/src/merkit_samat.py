def samat(text, int1, int2):
    if int1 >= len(text) or int2 >= len(text):
        return False
    return text[int1] == text[int2]

if __name__ == "__main__":
    print(samat("abc", 1, 3))

if __name__ == "__main__":
    print(samat("coder", 1, 2))