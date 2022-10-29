# Kirjoita ratkaisu tähän
factorial = 1
while True:
    number = int(input("Anna luku: "))
    if number <= 0:
        break
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"Luvun {number} kertoma on {factorial}")
    factorial = 1
print("Kiitos ja moi!")