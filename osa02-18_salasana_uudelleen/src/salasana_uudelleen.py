# Kirjoita ratkaisu tähän
password1 = input("Salasana: ")

while True:
    password2 = input("Toista salasana: ")

    if password1 != password2:
        print("Ei ollut sama!")
    else:
        break
print("Käyttäjätunnus luotu!")