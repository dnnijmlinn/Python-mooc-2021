# Kirjoita ratkaisu tähän

story = ""
last = ""
while True:
    word = input("Anna sana: ")
    if word == "loppu" or word == last:
        break
    story = story + word + " "
    last = word
print(story)