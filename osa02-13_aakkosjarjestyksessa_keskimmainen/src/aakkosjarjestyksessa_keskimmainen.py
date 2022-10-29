# Kirjoita ratkaisu tähän
letter1 = input("Anna 1. kirjain:")
letter2 = input("Anna 2. kirjain:")
letter3 = input("Anna 3. kirjain:")

if letter1 > letter2 > letter3 or letter1 < letter2 < letter3:
    middle = letter2
elif letter2 > letter1 > letter3 or letter2 < letter1 < letter3:
    middle = letter1
elif letter1 > letter3 > letter2 or letter1 < letter3 < letter2:
    middle = letter3
print(f"Keskimmäinen kirjain on {middle}")