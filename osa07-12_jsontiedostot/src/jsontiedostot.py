import json

def tulosta_henkilot(tiedosto:str):
    with open (tiedosto) as tiedosto:
        data = tiedosto.read()
        opiskelijat = json.loads(data)
    
    for opiskelija in opiskelijat:
        lista = opiskelija["harrastukset"]
        yhd = ", ".join(lista)

        for alkio in lista:
            alkio.replace("\n", "")
        
        print(f'{opiskelija["nimi"]} {opiskelija["ika"]} vuotta ({yhd})')

#main
if __name__ == "__main__":
    tulosta_henkilot("tiedosto1.json")