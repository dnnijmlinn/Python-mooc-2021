# Kirjoita ratkaisu tähän

print("Henkilö 1:")
name1 = input("Nimi: ")
age1 = int(input("Ikä: "))

print("Henkilö 2:")
name2 = input("Nimi: ")
age2 = int(input("Ikä: "))

if age1 > age2:
    print(f"Vanhempi on {name1}")
elif age2 > age1:
    print(f"Vanhempi on {name2}")
else:
    print(f"{name1} ja {name2} ovat yhtä vanhoja")