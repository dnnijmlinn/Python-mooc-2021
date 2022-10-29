# Kirjoita ratkaisu tähän
num = int(input("Anna pisteet [0-100]:"))
if num < 0 or num > 100:
    print("Arvosana: mahdotonta!")
elif num < 49:
    print("Arvosana: hylätty")
elif num > 49 and num <= 59:
    print("Arvosana: 1")
elif num >= 60 and num <= 69:
    print("Arvosana: 2")
elif num >= 70 and num <= 79:
    print("Arvosana: 3")
elif num >= 80 and num <= 89:
    print("Arvosana: 4")
elif num >= 90 and num <= 100:
    print("Arvosana: 5")