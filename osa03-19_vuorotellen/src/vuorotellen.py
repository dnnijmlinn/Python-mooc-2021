# Kirjoita ratkaisu tähän
number = int(input("Anna luku: "))
 
left = 1
right = number
 
while left < right:
    print(left)
    print(right)
    left += 1
    right -= 1
 
if left == right:
    print(left)