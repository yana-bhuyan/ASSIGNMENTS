n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

print("All movie details:", movies)

for name, details in movies.items():
    if details["year"] < 2015:
        print("Before 2015:", name)

for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print("Profitable movie:", name)

director_name = input("Enter director name to search: ")
for name, details in movies.items():
    if details["director"] == director_name:
        print("Movie by director:", name)