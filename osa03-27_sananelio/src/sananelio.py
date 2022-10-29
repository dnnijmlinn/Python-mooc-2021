def nelio(text, num):
    piste = []
    k = 0
    for i in text:
        piste += i

    for x in range(num):
        for y in range(num):
            i = piste[k]
            print(i, end=(''))
            k += 1
            if k == len(piste):
                k = 0
        print()



# Testing the function
if __name__ == "__main__":
    nelio("text", 3)