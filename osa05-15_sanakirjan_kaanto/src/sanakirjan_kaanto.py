# tee ratkaisu tänne
def kaanna(dictionary: dict):
    temp = {}
    
    for key, value in dictionary.items():
        temp[value] = key

    dictionary.clear()

    for key, value in temp.items():
        dictionary[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print(s)
    kaanna(s)
    print(s)