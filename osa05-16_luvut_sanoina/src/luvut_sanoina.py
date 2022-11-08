# tee ratkaisu tänne

def lukukirja():

    dictionary = {}
    numbers = []
    for initialise in range(100):
        numbers.append(initialise)

    #print(numbers)

    word0 = ['nolla']
    wordints = ['yksi', 'kaksi', 'kolme','neljä', 'viisi', 'kuusi','seitsemän', 'kahdeksan', 'yhdeksän']
    wordteens = ['kymmenen', 'yksitoista', 'kaksitoista', 'kolmetoista', 'neljätoista',
    'viisitoista', 'kuusitoista', 'seitsemäntoista', 'kahdeksantoista', 'yhdeksäntoista']
    wordtens = ['kaksikymmentä', 'kolmekymmentä', 'neljäkymmentä', 'viisikymmentä', 'kuusikymmentä', 'seitsemänkymmentä', 'kahdeksankymmentä', 'yhdeksänkymmentä']
    rest = []
    
    for i in range(len(wordtens)):
        rest.append(wordtens[i])
        for j in range(len(wordints)):
            rest.append(wordtens[i] + "" + wordints[j])
    
    wordListFinal = []
    wordListFinal.append(word0[0])
    for i in wordints:
        wordListFinal.append(i)
    for i in wordteens:
        wordListFinal.append(i)
    for i in rest:
        wordListFinal.append(i)
    #print(wordListFinal)

    dictionary = {numbers[i] : wordListFinal[i] for i in range(len(numbers))}

    return dictionary

if __name__ == "__main__":
    numbers = lukukirja()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])