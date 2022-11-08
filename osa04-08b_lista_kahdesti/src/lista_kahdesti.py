# Kirjoita ratkaisu tähän
list = []

while True:
    number = int(input("Anna luku: "))
    if number == 0:
        break
    list.append(number)
    print(f"Lista: {list}")
    print(f"Järjestettynä: {sorted(list)}")
print("Moi!")