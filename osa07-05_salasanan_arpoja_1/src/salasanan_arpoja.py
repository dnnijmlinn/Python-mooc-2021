# tee ratkaisu tänne

import string
from random import randint

def luo_salasana(pituus : int):
    lowercase_chars = list(string.ascii_lowercase)
    password = ''
    for i in range(pituus):
        random_index = randint(0, len(lowercase_chars)-1)
        password += lowercase_chars[random_index]

    return password

if __name__ == "__main__":
    for i in range(100):
        print(luo_salasana(18))