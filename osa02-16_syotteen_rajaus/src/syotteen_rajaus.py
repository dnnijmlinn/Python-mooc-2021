from math import sqrt
# Kirjoita ratkaisu tähän

while True:
    number = int(input("Syötä luku: "))
    if number == 0:
        break
    elif number < 0:
        print("Epäkelpo luku")
    else:
        print(sqrt(number))
print("Lopetetaan...")