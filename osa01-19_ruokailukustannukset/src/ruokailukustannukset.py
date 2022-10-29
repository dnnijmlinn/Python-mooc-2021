# Kirjoita ratkaisu tähän
times = int(input("Montako kertaa viikossa syöt Unicafessa? "))
price = float(input("Unicafe-lounaan hinta? "))
groceries = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

daily = (times * price + groceries) / 7
weekly = times * price + groceries

print("Kustannukset keskimäärin:")
print(f"Päivässä {daily} euroa")
print(f"Viikossa {weekly} euroa")