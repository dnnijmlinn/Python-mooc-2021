# Tee ratkaisu tänne
def anagrammi(word1 : str, word2 : str):
    sorted1 = sorted(word1)
    sorted2 = sorted(word2)
    if sorted1 == sorted2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrammi("tame", "meta")) # True
    print(anagrammi("tame", "mate")) # True
    print(anagrammi("tame", "team")) # True
    print(anagrammi("tabby", "batty")) # False
    print(anagrammi("python", "java")) # False