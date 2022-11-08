def read_file(file_name):
    with open(file_name) as diary:
        for line in diary:
            print(line.replace('\n', ''))
        diary.close()

def update_file(file_name, entry):
    with open(file_name, 'a') as diary:
        diary.write(entry + '\n')
        diary.close()

while True:
    print('1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta')
    choice = int(input('Valinta: '))
    if choice == 1:
        entry = input('Anna merkintä: ')
        update_file('paivakirja.txt', entry)
        print('Päiväkirja tallennettu')
    elif choice == 2:
        read_file('paivakirja.txt')
    elif choice == 0:
        print('Heippa!')
        break