ыф# Kirjoita ratkaisu tähän
word1 = input("Anna jono 1: ")
word2 = input("Anna jono 2: ")

if len(word1) > len(word2):
    print(f"{word1} on pidempi")
elif len(word2) > len(word1): 
    print(f"{word2} on pidempi")
else:
    print("Jonot ovat yhtä pitkät")