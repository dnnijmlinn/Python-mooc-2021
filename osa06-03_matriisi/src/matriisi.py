# tee ratkaisu tänne

def list_total(nums):
    total = 0
    for n in nums:
        total += n
    return total

def list_max(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def summa():
    with open("matriisi.txt") as file:
        file_total = 0
        for line in file:
            line = line.replace('\n','')
            nums_str = line.split(',')
            nums = []
            for n in nums_str:
                nums.append(int(n))
            file_total += list_total(nums)
        return file_total

def maksimi():
    with open("matriisi.txt") as file:
        file_max = -100000000
        for line in file:
            line = line.replace('\n','')
            nums_str = line.split(',')
            nums = []
            for n in nums_str:
                nums.append(int(n))
            if list_max(nums) > file_max:
                file_max = list_max(nums)
        return file_max

def rivisummat():
    with open("matriisi.txt") as file:
        file_row_sums = []
        for line in file:
            line = line.replace('\n','')
            nums_str = line.split(',')
            nums = []
            for n in nums_str:
                nums.append(int(n))
            file_row_sums.append(list_total(nums))
        return file_row_sums

if __name__ =="__main__":
    print(summa())
    print(maksimi())
    print(rivisummat())