# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
def palindromi(string):
    return string == string[::-1]

def main():
    while True:
        word = input("Anna palindromi: ")
        if palindromi(word):
            print(f"{word} on palindromi!")
            break
        print("ei ollut palindromi")
main()
