# tee ratkaisu tänne

def lue_hedelmat():
    my_dictionary = {}
    with open("hedelmat.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            my_dictionary[parts[0]] = float(parts[1])
            
    return my_dictionary

if __name__ == "__main__":
    print(lue_hedelmat())