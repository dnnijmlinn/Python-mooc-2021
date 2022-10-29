# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

x1 = (-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)
x2 = (-b - sqrt(b ** 2 - (4 * a * c))) / (2 * a)
print(f"The roots are {x1} and {x2}")