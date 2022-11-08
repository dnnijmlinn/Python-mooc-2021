# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):
    if nimi == '' or len(nimi.split(' ')) < 2 or len(nimi) > 40 or ika < 0 or ika > 150:
        raise ValueError('ValueError')
    return (nimi, ika)