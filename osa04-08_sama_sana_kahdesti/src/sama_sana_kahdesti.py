# Kirjoita ratkaisu tähän
list = []
while True:
    word = input("sana: ")
    if word in list:
        print(f"Annoit {len(list)} eri sanaa")
        break
    list.append(word)