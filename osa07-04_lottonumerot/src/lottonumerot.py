# tee ratkaisu tänne

from random import randint

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    numbers = []
    while len(numbers) < maara:
        number = randint(alaraja, ylaraja)
        if number not in numbers:
            numbers.append(number)
 
    return sorted(numbers)

if __name__ == "__main__":
    for number in lottonumerot(7, 1, 40):
        print(number)