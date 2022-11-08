# tee ratkaisu tänne

from datetime import datetime


def calculate_age(year: int, month: int, day: int):
    birthday = datetime(year, month, day)
    millenium = datetime(1999, 12, 31)
    difference = millenium - birthday
    return difference.days

day = int(input('Päivä: '))
month = int(input('Kuukausi: '))
year = int(input('Vuosi: '))

age_by_millenium = calculate_age(year, month, day)
if age_by_millenium > 0:
    print(f'Olit {age_by_millenium} päivää vanha, kun vuosituhat vaihtui.')
else:
    print(f"Et ollut syntynyt, kun vuosituhat vaihtui.")