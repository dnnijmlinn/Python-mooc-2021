def luvuista_suurin(num1,num2,num3):
    list1 = []
    list1.append(num1)
    list1.append(num2)
    list1.append(num3)

    return max(list1)
    
if __name__ == "__main__":
    prt = luvuista_suurin(5, 4, 8)
    print(prt)