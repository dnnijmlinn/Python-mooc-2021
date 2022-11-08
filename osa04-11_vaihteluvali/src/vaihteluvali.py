def vaihteluvali(list : list):
    minimal = min(list)
    maximal = max(list)
    return maximal - minimal
    
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)