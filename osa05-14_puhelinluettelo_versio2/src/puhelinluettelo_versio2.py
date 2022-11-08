# tee ratkaisu tänne

def search(phonebook):
    name = input("name: ")
    if name not in phonebook:
        print("ei numeroa")
    else:
        for num in phonebook[name]:
            print(num)

def add(phonebook):
    name = input("name: ")
    number = input("number: ")

    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(number)

    print("ok!")

def main():
    phonebook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            search(phonebook)
        if command == 2:
            add(phonebook)
        if command == 3:
            break
    print("lopetetaan...")

main()