import csv
from datetime import datetime, timedelta

def viralliset_pisteet():
    with open("tentin_aloitus.csv") as aloitus, open("palautus.csv") as palautus:
        aloitusajat = {}
        # Luetaan ensin opiskelijat ja aloitusajat muistiin
        for rivi in csv.reader(aloitus, delimiter=";"):
            nimi = rivi[0]
            aika = datetime.strptime(rivi[1], "%H:%M")
            aloitusajat[nimi] = aika

        # Luetaan sitten palautukset
        # Jokaiselta opiskelijalta tallennetaan sanakirjaan jokaisesta tehtävästä
        # aika ja pistemäärä. Aika ja pistemäärä tallennetaan tuplena.
        pisteet = {}
        for rivi in csv.reader(palautus, delimiter=";"):
            nimi = rivi[0]
            tehtavanro = int(rivi[1])
            pist = int(rivi[2])
            aika = datetime.strptime(rivi[3], "%H:%M")

            # Jos kyseessä on huijaus, palautusta ei käsitellä
            if aika - aloitusajat[nimi] > timedelta(hours=3):
                continue
            
            # Jos ei ole vielä käsitelty tätä opiskelijaa, lisätään suoraan
            if nimi not in pisteet:
                oletusaika = datetime(1900, 1, 1)
                pisteet[nimi] = {}
                for i in range(1, 8 + 1):
                    pisteet[nimi][i] = 0
                pisteet[nimi][tehtavanro] = pist

            
            # Jos on jo lisätty opiskelija, pisteitä tulee olla aiempaa enemmän
            if pist > pisteet[nimi][tehtavanro]:
                pisteet[nimi][tehtavanro] = pist 
        
        # Käydään läpi kaikki opiskelijat yksi kerrallaan
        lopulliset_pisteet = {}
        for opiskelija in pisteet:
            pist = 0
            for tehtava in pisteet[opiskelija]:
                pist += pisteet[opiskelija][tehtava]
            lopulliset_pisteet[opiskelija] = pist
        return lopulliset_pisteet 

#main
if __name__ == "__main__":
    print(viralliset_pisteet())