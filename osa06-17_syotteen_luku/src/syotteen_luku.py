# tee ratkaisu tänne
def lue(pyynto, ala, yla):
    while True:
        try:
            num = int(input(pyynto))
            if num >= ala and num <= yla:
                return num
        except ValueError:
            pass

        print(f'Syötteen on oltava kokonaisluku väliltä {ala} ... {yla}')