# tee ratkaisu tänne
def compare_dot(word_with_dot, word):
    same = True
    for i in range(len(word)):
        if word_with_dot[i] != '.' and word_with_dot[i] != word[i]:
            same = False
    return same

def hae_sanat(hakusana: str):
    found_terms = []

    with open('sanat.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            word = line.strip()
            if ('.' in hakusana) and len(hakusana) == len(word):
                if compare_dot(hakusana, word) == True:
                    found_terms.append(word)
            elif hakusana.startswith('*'):
                if word.endswith(hakusana[1:]):
                    found_terms.append(word)
            elif hakusana.endswith('*'):
                if word.startswith(hakusana[:-1]):
                    found_terms.append(word)
            else:
                if hakusana == word:
                    found_terms.append(word)

    return found_terms
    
if __name__ == "__main__":
    print(hae_sanat('acq*'))