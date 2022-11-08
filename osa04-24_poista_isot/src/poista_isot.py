# tee ratkaisu tänne
from curses.ascii import isupper


def poista_isot(list : list):
    new_list = []
    for i in list:
        if i.isupper():
            continue
        else:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = poista_isot(my_list)
    print(pruned_list)