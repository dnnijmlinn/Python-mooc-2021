# tee ratkaisu tänne
from math import sqrt

def hypotenuusa(leg1: float, leg2: float):
    return sqrt(leg1 * leg1 + leg2 * leg2)

if __name__ == "__main__":
    print(hypotenuusa(3,4)) # 5.0
    print(hypotenuusa(5,12)) # 13.0
    print(hypotenuusa(1,1)) # 1.4142135623730951