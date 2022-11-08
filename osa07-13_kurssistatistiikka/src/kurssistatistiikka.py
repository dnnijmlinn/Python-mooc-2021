import urllib.request
import json

def hae_kaikki():
    pyynto = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    kurssi_data = json.loads(pyynto.read())
    kurssit = []
    for kurssi in kurssi_data:
        if not kurssi['enabled']:
            continue
 
        harjoituksia = sum(kurssi['exercises'])
        kurssit.append((kurssi['fullName'], kurssi['name'], kurssi['year'], harjoituksia))
 
    return kurssit
 
def hae_kurssi(kurssi: str):
    pyynto = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats")
    kurssin_viikot = json.loads(pyynto.read())
    opiskelijoita = 1
    tehtavia = 0
    tunteja = 0 
    for nro, viikko in kurssin_viikot.items():
        if viikko['students'] > opiskelijoita:
            opiskelijoita = viikko['students']
        tunteja += viikko['hour_total']
        tehtavia += viikko['exercise_total']
 
    return {
        "viikkoja": len(kurssin_viikot),
        "opiskelijoita": opiskelijoita,
        "tunteja": tunteja,
        "tunteja_keskimaarin": tunteja//opiskelijoita,
        "tehtavia": tehtavia,
        "tehtavia_keskimaarin": tehtavia//opiskelijoita,
    }

#main
if __name__ == "__main__":
    print(hae_kaikki())
    print(hae_kurssi("fullstack2019"))