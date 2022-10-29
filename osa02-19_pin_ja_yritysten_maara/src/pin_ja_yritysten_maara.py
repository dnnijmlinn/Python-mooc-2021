# Kirjoita ratkaisu tähän
atemps = 0
while True:
    pin = int(input("PIN-koodi: "))
    atemps += 1
    if pin == 4321:
        break
    print("Väärin")
if atemps == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {atemps} yritystä")