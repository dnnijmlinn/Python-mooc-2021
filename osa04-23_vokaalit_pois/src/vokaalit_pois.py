# tee ratkaisu tänne
def ilman_vokaaleja(string):
    vowels = ["ä","ö","e","i","a","u","å","y","o"]
    word = ""
    for i in string:
        if i in vowels:
            i = ""
        word += i
    return word



if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))