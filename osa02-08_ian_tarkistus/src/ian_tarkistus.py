# Kirjoita ratkaisu tähän
age = int(input("Kerro ikäsi?"))
if age < 0:
    print("Taitaa olla virhe")
elif age < 5:
    print("En usko, että osaat kirjoittaa...")
else:
    print(f"Ok, olet siis {age}-vuotias")  