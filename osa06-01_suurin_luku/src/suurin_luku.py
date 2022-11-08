# tee ratkaisu tänne
def suurin():
    with open("luvut.txt") as new_file:
        suurin = ""
        for line in new_file:
            line = line.replace("\n", "")
            if suurin < line:
                suurin = line
    return(int(suurin))
            
if __name__ == "__main__":            
    suurin()