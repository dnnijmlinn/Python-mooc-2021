# tee ratkaisu tänne
def etsi_elokuvat(database: list, search_term: str):
    movies = []

    for movie in database:
        if search_term in movie['nimi'].lower():
            movies.append(movie)

    return movies
    
if __name__ == "__main__":
    database = [{"nimi": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"nimi": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"nimi": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = etsi_elokuvat(database, "python")
    print(my_movies)