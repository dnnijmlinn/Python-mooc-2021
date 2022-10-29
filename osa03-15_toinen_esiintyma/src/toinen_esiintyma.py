string = input("Anna merkkijono: ")
substring = input("Anna osajono: ")

index1 = string.find(substring)
index2 = -1
if index1 != -1:
    index2 = string.find(substring, index1 + len(substring))

if index2 == -1:
    print('Osajono ei esiinny merkkijonossa kahdesti.')
else:
    print(f"Osajonon toinen esiintymä on kohdassa {index2}.")