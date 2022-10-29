# Kirjoita ratkaisu tähän
word = input("Anna sana: ")
second = word[1]
secondLast = word[-2]

if second != secondLast:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")
else:
    print(f"Toinen ja toiseksi viimeinen kirjain on {second}")