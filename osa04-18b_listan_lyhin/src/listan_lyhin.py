# tee ratkaisu tänne
def lyhin(my_list : list):
    lyhin = my_list[0]
    for i in my_list:
        if len(i) <= len(lyhin):
            lyhin = i
    return lyhin
    
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = lyhin(my_list)
    print(result)