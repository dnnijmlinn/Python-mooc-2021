# Kirjoita ratkaisu tähän

word1 = input("Anna 1. sana:")
word2 = input("Anna 2. sana:")

if word1 > word2:
    print(f"{word1} on aakkosjärjestyksessä viimeinen.")
elif word2 > word1:
    print(f"{word2} on aakkosjärjestyksessä viimeinen.")
else:
    print("Annoit saman sanan kahdesti.")