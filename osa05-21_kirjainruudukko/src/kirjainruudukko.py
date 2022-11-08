# Kirjoita ratkaisu tähän
n = int(input("Layers: "))
 
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
left = ""    
right = ""   
k = n-1       
m = 2*n-1    
while k >= 1:
    left = left+alphabets[k]
    right = alphabets[k]+right
    m -= 2
    print(left+alphabets[k]*m+right)
    k -= 1
while k <= n-1:
    print(left+alphabets[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1