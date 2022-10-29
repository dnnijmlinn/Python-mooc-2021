# Kirjoita ratkaisu tähän
num = int(input("Please type in a temperature (F):"))
celsius = (num - 32) * 5.0/9.0
print(f"{num} fahrenheit-astetta on {celsius} celsius-astetta")
if celsius < 0:
    print("Paleltaa!")