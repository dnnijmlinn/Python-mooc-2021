# tee ratkaisu tänne
def arvo(x, data):
    merkit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in merkit:
        return data[merkit.index(x)]
    else:
        return int(x)

#ehdot IF valinnalle main ohjelmassa
def ehto(a, ehto, b):
    if ehto == "==":
        return a == b
    if ehto == "!=":
        return a != b
    if ehto == "<":
        return a < b
    if ehto == "<=":
        return a <= b
    if ehto == ">":
        return a > b
    if ehto == ">=":
        return a >= b


def suorita(ohjelma):
    pituus = len(ohjelma)
    rivi = 0
    merkit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    tulos = []

    while True:
        if rivi == pituus:
            break
        osat = ohjelma[rivi].split(" ")
        if osat[0] == "PRINT":  # PRINT [arvo]: tulostaa annetun arvon
            tulos.append(arvo(osat[1], data))
        if osat[0] == "MOV":    # MOV [muuttuja] [arvo]: asettaa muuttujaan annetun arvon
            data[merkit.index(osat[1])] = arvo(osat[2], data)
        if osat[0] == "ADD":    # ADD [muuttuja] [arvo]: lisää muuttujaan annetun arvon
            data[merkit.index(osat[1])] += arvo(osat[2], data)
        if osat[0] == "SUB":    # SUB [muuttuja] [arvo}: vähentää muuttujasta annetun arvon
            data[merkit.index(osat[1])] -= arvo(osat[2], data) 
        if osat[0] == "MUL":    # MUL [muuttuja] [arvo]: kertoo muuttujan annetulla arvolla
            data[merkit.index(osat[1])] *= arvo(osat[2], data)
        if osat[0] == "JUMP":   # JUMP [kohta]: hyppää annettuun kohtaan
            rivi = ohjelma.index(osat[1]+":")
            continue
        if osat[0] == "IF": # IF [ehto] JUMP [kohta]: jos ehto pätee, hyppää annettuun kohtaan
            if ehto(arvo(osat[1], data), osat[2], arvo(osat[3], data)):
                rivi = ohjelma.index(osat[5]+":")
                continue
        if osat[0] == "END":
            break
        rivi += 1
    return tulos


#main
if __name__ == "__main__":
    ohjelma1 = []
    ohjelma1.append("MOV A 1")
    ohjelma1.append("MOV B 2")
    ohjelma1.append("PRINT A")
    ohjelma1.append("PRINT B")
    ohjelma1.append("ADD A B")
    ohjelma1.append("PRINT A")
    ohjelma1.append("END")
    tulos = suorita(ohjelma1)
    print("Ohjelma1:", tulos)    #[1, 2, 3]

    ohjelma2 = []
    ohjelma2.append("MOV A 1")
    ohjelma2.append("MOV B 10")
    ohjelma2.append("alku:")
    ohjelma2.append("IF A >= B JUMP loppu")
    ohjelma2.append("PRINT A")
    ohjelma2.append("PRINT B")
    ohjelma2.append("ADD A 1")
    ohjelma2.append("SUB B 1")
    ohjelma2.append("JUMP alku")
    ohjelma2.append("loppu:")
    ohjelma2.append("END")
    tulos = suorita(ohjelma2)
    print("Ohjelma2:", tulos)    #[1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

    ohjelma3 = []
    ohjelma3.append("MOV A 1")
    ohjelma3.append("MOV B 1")
    ohjelma3.append("alku:")
    ohjelma3.append("PRINT A")
    ohjelma3.append("ADD B 1")
    ohjelma3.append("MUL A B")
    ohjelma3.append("IF B <= 10 JUMP alku")
    ohjelma3.append("END")
    tulos = suorita(ohjelma3)
    print("Ohjelma3 (kertoma):", tulos)

    ohjelma4 = []
    ohjelma4.append("MOV N 50")
    ohjelma4.append("PRINT 2")
    ohjelma4.append("MOV A 3")
    ohjelma4.append("alku:")
    ohjelma4.append("MOV B 2")
    ohjelma4.append("MOV Z 0")
    ohjelma4.append("testi:")
    ohjelma4.append("MOV C B")
    ohjelma4.append("uusi:")
    ohjelma4.append("IF C == A JUMP virhe")
    ohjelma4.append("IF C > A JUMP ohi")
    ohjelma4.append("ADD C B")
    ohjelma4.append("JUMP uusi")
    ohjelma4.append("virhe:")
    ohjelma4.append("MOV Z 1")
    ohjelma4.append("JUMP ohi2")
    ohjelma4.append("ohi:")
    ohjelma4.append("ADD B 1")
    ohjelma4.append("IF B < A JUMP testi")
    ohjelma4.append("ohi2:")
    ohjelma4.append("IF Z == 1 JUMP ohi3")
    ohjelma4.append("PRINT A")
    ohjelma4.append("ohi3:")
    ohjelma4.append("ADD A 1")
    ohjelma4.append("IF A <= N JUMP alku")
    tulos = suorita(ohjelma4)
    print("Ohjelma4 (alkuluvut):", tulos)