# tee ratkaisu tänne
import difflib

def wordlist():
    words = []
    with open("wordlist.txt") as tiedosto:
        for rivi in tiedosto:
            words.append(rivi.strip())
    return words

words = wordlist()
lause = input("write text: ")
virhe = []
for sana in lause.split(' '):
    if sana.lower() in words:
        print(sana+ " ", end="")
    else:
        virhe.append(sana)
        print("*" + sana+ "* ", end="")


# Korjausehdotukset etsitään standardikirjaston moduulin difflib tarjoaman funktion get_close_matches avulla.
print()
print("korjausehdotukset:")
for sana in virhe:
    korjaus_lista = difflib.get_close_matches(sana, words)
    korjaukset = ", ".join(korjaus_lista)
    print(f"{sana}: {korjaukset}")

#main
# if __name__ == "__main__":
#     print(wordlist())