# Kirjoita ratkaisu tähän
list = []
while True:
    print(f"Lista on nyt {list}")
    selection = input("(l)isää, (p)oista vai e(x)it:")
    if selection == "l":

        item = len(list) + 1
        list.append(item)
    elif selection == "p":
        list.pop(len(list) - 1)
    elif selection == "x":
        break
    
print("Moi!")