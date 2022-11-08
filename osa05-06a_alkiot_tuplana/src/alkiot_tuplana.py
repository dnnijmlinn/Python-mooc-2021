# tee ratkaisu tänne

def tuplaa_alkiot(my_list : list):
    new_list = []
    for item in my_list:
        new_list.append(item * 2)

    return new_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = tuplaa_alkiot(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)