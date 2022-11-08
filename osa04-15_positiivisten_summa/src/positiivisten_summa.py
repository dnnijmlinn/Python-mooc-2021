# tee ratkaisu tänne

def positiivisten_summa(my_list):
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i     
    return sum

if __name__ == "__main__":
    print(positiivisten_summa([1, -1, 2, -2, 3, -3]))