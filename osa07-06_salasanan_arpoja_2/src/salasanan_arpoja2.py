# tee ratkaisu tänne

from random import choice, randint
from string import ascii_lowercase, digits
 
def luo_hyva_salasana(pituus: int, numerot: bool, erikoismerkit: bool):
    special_chars = "!?=+-()#"
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
 
    if numerot:
        passwd = add_character(passwd, digits)
        choice_set += digits
 
    if erikoismerkit:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
 
    while (len(passwd) < pituus):
        passwd = add_character(passwd, choice_set)
 
    return passwd
 
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character

if __name__ == "__main__":
    for i in range(10):
        print(luo_hyva_salasana(5, False, True))