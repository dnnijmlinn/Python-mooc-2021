# tee ratkaisu tänne

from string import ascii_letters, digits

def vaihda_koko(merkkijono: str):
    uusimerkkijono = ""
    for merkki in merkkijono:
        if merkki.islower():
            uusimerkkijono += merkki.upper()
        elif merkki.isupper():
            uusimerkkijono += merkki.lower()
        else:
            uusimerkkijono += merkki
    return uusimerkkijono

# Palauttaa tuplessa parametrinaan saamansa merkkijonon ensimmäisen ja toisen puolikkaan. 
# Jos merkkijonossa on pariton määrä kirjaimia, ensimmäinen puolikas on lyhyempi.
def puolita(merkkijono: str):
    return merkkijono[:len(merkkijono) // 2], merkkijono[len(merkkijono) // 2:]

# Palauttaa merkkijonon, josta on poistettu kaikki muut merkit paitsi aakkoset [a...ö, A...Ö], numerot ja välilyönnit.
def poista_erikoismerkit(merkkijono: str):
    sallitut = ascii_letters + digits + "ÅåÄäÖö "
    uusimerkkijono = ""
    for merkki in merkkijono:
        if merkki in sallitut:
            uusimerkkijono += merkki
    return uusimerkkijono

#main
if __name__ == "__main__":
    import merkkiapuri
    print("Vaihdetaan kirjaimien koko:")
    print(vaihda_koko("hEi MaailmA ON hieno aamu OHJELmoida"))
    print("Puolitetaan merkkijono:")
    print(puolita("Puolitetaan annettu merkkijono..."))
    print("Poistetaan merkkijonosta erikoismerkit:")
    print(poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!"))