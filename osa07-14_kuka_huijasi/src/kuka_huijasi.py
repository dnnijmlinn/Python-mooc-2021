import csv
from datetime import datetime, timedelta
def huijarit():
    with open("tentin_aloitus.csv") as aloitus, open("palautus.csv") as palautus:
        aloitusajat = {}
        # Luetaan ensin opiskelijat ja aloitusajat muistiin
        for rivi in csv.reader(aloitus, delimiter=";"):
            nimi = rivi[0]
            aika = datetime.strptime(rivi[1], "%H:%M")
            aloitusajat[nimi] = aika

        # Luetaan sitten palautukset (Jokaiselta opiskelijalta tallennetaan viimeinen (eli suurin) aika)
        palautusajat = {}
        for rivi in csv.reader(palautus, delimiter=";"):
            nimi = rivi[0]
            aika = datetime.strptime(rivi[3], "%H:%M")
            # Jos ei ole vielä käsitelty tätä opiskelijaa, lisätään suoraan
            if nimi not in palautusajat:
                palautusajat[nimi] = aika
            # Jos on jo lisätty aika, katsotaan onko käsiteltävä aika "suurempi"
            elif aika >  palautusajat[nimi]:
                palautusajat[nimi] = aika
        
        huijarit = []
        # Käydään läpi kaikki opiskelijat yksi kerrallaan
        for nimi in aloitusajat:
            if palautusajat[nimi] - aloitusajat[nimi] > timedelta(hours = 3):
                huijarit.append(nimi)
        return huijarit 

#main
if __name__ == "__main__":
    print(huijarit())