word = input("Anna sana: ")
i = -1
sum =""
while i >= -len(word):
    sum = word[i] + sum
    print(sum)
    i -= 1