# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def keskiarvo(list : list):
    i = 0
    sum = 0
    while i < len(list):
        sum += list[i]
        i += 1
    return sum/len(list)

if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)
