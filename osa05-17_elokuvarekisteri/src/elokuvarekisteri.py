# tee ratkaisu tänne
def lisaa_elokuva(database: list, name: str, director: str, year: int, runtime: int):
    movie = {}
    movie = {"nimi" : name, "ohjaaja" : director, "vuosi" : year, "pituus" : runtime}
    database.append(movie)
    
if __name__ == "__main__":
    database = []
    lisaa_elokuva(database, "Gone with the Python", "Victor Pything", 2017, 116)
    lisaa_elokuva(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)