# tee ratkaisu tänne

from random import choice

def heita(die: str):
    if die == "A":
        options = [3, 3, 3, 3, 3, 6]
        rand = choice(options)
    elif die == "B":
        options = [2, 2, 2, 5, 5, 5]
        rand = choice(options)
    elif die == "C":
        options = [1, 4, 4, 4, 4, 4]
        rand = choice(options)
    return rand

def pelaa(die1: str, die2: str, times: int):
    die1_win_count = 0
    die2_win_count = 0
    for i in range(times):
        die1_result = heita(die1)
        die2_result = heita(die2)
        if die1_result > die2_result:
            die1_win_count += 1
        elif die2_result > die1_result:
            die2_win_count += 1
    draw = times - (die1_win_count + die2_win_count)
    return (die1_win_count, die2_win_count, draw)


if __name__ == "__main__":
    for i in range(20):
        print(heita("A"), " ", end="")
    print()

    for i in range(20):
        print(heita("B"), " ", end="")
    print()

    for i in range(20):
        print(heita("C"), " ", end="")
    print()
    
    result = pelaa("A", "C", 1000)
    print(result)
    result = pelaa("B", "B", 1000)
    print(result)