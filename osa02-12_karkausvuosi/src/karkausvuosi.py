# Kirjoita ratkaisu tähän
num = int(input("Anna vuosi:"))
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")