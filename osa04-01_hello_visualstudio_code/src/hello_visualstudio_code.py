# Kirjoita ratkaisu tähän
while True:
    editor = input("Editori: ")

    if editor.lower() == "notepad" or editor.lower() == "word":
        print("surkea")
    elif editor.lower() == "visual studio code":
        print("loistava valinta!")
        break
    else:
        print("ei ole hyvä")