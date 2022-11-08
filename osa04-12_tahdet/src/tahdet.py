# tee ratkaisu tänne
def lista_tahtina(list : list):
    size = len(list)
    i = 0
    while i < size:
        print("*" * list[i])
        i += 1
        
if __name__ == "__main__":
    lista_tahtina([3, 7, 1, 1, 2])