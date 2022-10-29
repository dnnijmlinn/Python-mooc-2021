# Kirjoita ratkaisu tähän
sum = int(input("Lahjan suuruus?"))

if sum < 5000:
    print("Ei veroa!")
elif sum >= 5000 and sum < 25000:
    tax = 100 + (sum - 5000) * 0.08
    print(f"Vero: {tax} euroa")
elif sum >= 25000 and sum < 55000:
    tax = 1700 + (sum - 25000) * 0.10
    print(f"Vero: {tax} euroa")
elif sum >= 55000 and sum < 200000:
    tax = 4700 + (sum - 55000) * 0.12
    print(f"Vero: {tax} euroa")
elif sum >= 200000 and sum < 1000000:
    tax = 22100 + (sum - 200000) * 0.15
    print(f"Vero: {tax} euroa")
else:
    tax = 142100 + (sum - 1000000) * 0.17
    print(f"Vero: {tax} euroa")