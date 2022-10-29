# Kirjoita ratkaisu tähän
wage = float(input("Tuntipalkka:"))
hours = int(input("Työtunnit:"))
day = input("Viikonpäivä:")

payment = wage * hours
if day == "sunnuntai":
    payment *= 2
print(f"Palkka {payment} euroa")