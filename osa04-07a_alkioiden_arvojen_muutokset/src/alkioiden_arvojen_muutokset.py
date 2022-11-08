list = [1,2,3,4,5]

while True:
    index = int(input("indeksi: "))

    if index == -1:
        break
    if index < 0 or index >= len(list):
        print("")
        continue
    newValue = int(input("uusi value: "))
    list[index] = newValue
    print(list)