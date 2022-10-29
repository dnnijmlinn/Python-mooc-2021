# Kirjoita ratkaisu tähän
count = 0
sum = 0
positive = 0
negative = 0
print("Syötä kokonaislukuja, 0 lopettaa:")
while True:
    num = int(input("Luku:"))
    if num == 0:
        break
    count += 1
    print(f"Lukuja yhteensä {count}")
    sum += num
    print(f"Lukujen summa {sum}")
    mean = sum / count
    print(f"Lukujen keskiarvo {mean}")
    if num > 0:
        positive += 1
    else:
        negative += 1
print(f"Positiivisia {positive}")
print(f"Negatiivisia {negative}")  