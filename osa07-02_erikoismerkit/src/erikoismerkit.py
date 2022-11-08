# tee ratkaisu tänne

from string import ascii_letters, punctuation

def jaa_merkkeihin(my_string: str):
    first = ''
    second = ''
    third = ''
    for character in my_string:
        if character in ascii_letters:
            first += character
        elif character in punctuation:
            second += character
        else:
            third += character
    return (first, second, third)

if __name__ == "__main__":
    parts = jaa_merkkeihin("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])