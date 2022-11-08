# tee ratkaisu tänne
from operator import contains


def uniikit(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
 
    results.sort()
    return results

if __name__ == "__main__":

    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(my_list))