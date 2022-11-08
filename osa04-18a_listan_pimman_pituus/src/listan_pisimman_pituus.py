# tee ratkaisu tänne
def pisimman_pituus(my_list : list):
    longest = len(my_list[0])
    for i in my_list:
        if len(i) >= longest:
            longest = len(i)
    return longest
    
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = pisimman_pituus(my_list)
    print(result)