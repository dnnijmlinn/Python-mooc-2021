# tee ratkaisu tänne

def pisin(list : list):
    longest = list[0]
    for word in list:
        if len(word) > len(longest):
            longest = word
    return longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(pisin(strings))