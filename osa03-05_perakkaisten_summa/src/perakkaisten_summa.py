# Kirjoita ratkaisu tähän
limit = int(input("Mihin asti:"))
num = 1
value = 1
x = "1"
while value < limit:
    num += 1
    value += num
    x += f" + {num}"
print(f"Laskettiin {x} = {value}")