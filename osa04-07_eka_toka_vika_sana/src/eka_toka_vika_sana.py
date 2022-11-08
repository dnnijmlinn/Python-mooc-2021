def eka_sana(text):
    sanat = text.split(" ")
    return sanat[0]

def toka_sana(text):
    sanat = text.split(" ")
    return sanat[1]

def vika_sana(text):
    sanat = text.split(" ")
    return sanat[-1]

if __name__ == "__main__":
    sentence = ""
    print(eka_sana(sentence))
    print(toka_sana(sentence))
    print(vika_sana(sentence))