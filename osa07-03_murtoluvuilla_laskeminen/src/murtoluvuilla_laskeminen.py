# tee ratkaisu tänne

from fractions import Fraction

def jaa_palasiksi(maara: int):
    fractions = []
    for i in range(maara):
        fractions.append(Fraction(1, maara))
    return fractions

if __name__ == "__main__":
    for p in jaa_palasiksi(3):
        print(p)

    print()
    print(jaa_palasiksi(5))