# tee ratkaisu tänne

def poista_pienin( my_list : list):
    smallest = my_list[0]
    for i in my_list:
        if i < smallest:
            smallest = i
    my_list.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    poista_pienin(numbers)
    print(numbers)