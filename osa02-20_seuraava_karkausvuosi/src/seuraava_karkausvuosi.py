# Kirjoita ratkaisu tähän
year = int(input("Vuosi:"))
nextYear = year + 1

while True:
    if nextYear % 4 == 0 and nextYear % 100 != 0 or nextYear % 400 == 0:
        break
    nextYear += 1
print(f"Vuotta {year} seuraava karkausvuosi on {nextYear}")   