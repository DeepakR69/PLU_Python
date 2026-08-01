# ### Problem Statement
# A streaming platform stores movie information.
# Each movie contains
# * Movie ID
# * Title
# * Genre
# * Rating
# * Watch Count
# ### Requirements
# 1. Fetch all movies.
# 2. Sort movies based on Rating.
# 3. Search a movie using Movie ID.
# 4. Display Top 10 highest-rated movies.
# 5. Display the most watched movie in every genre.
# ### Concepts
# * Sorting
# * Searching
# * Dictionaries
# * SQL GROUP BY
import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    movie_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    rating REAL,
    watch_count INTEGER
)
""")

movies = [
    (101, "Inception", "Sci-Fi", 8.8, 9500),
    (102, "Avengers", "Action", 8.4, 12000),
    (103, "Interstellar", "Sci-Fi", 8.9, 11000),
    (104, "Joker", "Drama", 8.5, 8000),
    (105, "Titanic", "Romance", 7.9, 15000),
    (106, "Bahubali", "Action", 8.2, 13000),
    (107, "3 Idiots", "Comedy", 8.4, 16000),
    (108, "KGF", "Action", 8.3, 14500),
    (109, "Dangal", "Sports", 8.5, 17000),
    (110, "Shershaah", "War", 8.4, 10000),
    (111, "Drishyam", "Thriller", 8.6, 9000),
    (112, "Pushpa", "Action", 7.8, 18000)
]

cursor.executemany(
    "INSERT OR REPLACE INTO movies VALUES(?,?,?,?,?)",
    movies
)

conn.commit()
conn.close()

print("Database Created Successfully")
import sqlite3


# --------------------------
# Movie Class
# --------------------------

class Movie:

    def __init__(self, movie_id, title, genre, rating, watch_count):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watch_count = watch_count

    def display(self):
        print(f"""
Movie ID     : {self.movie_id}
Title        : {self.title}
Genre        : {self.genre}
Rating       : {self.rating}
Watch Count  : {self.watch_count}
""")


# --------------------------
# Fetch Movies
# --------------------------

def fetch_movies():

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")

    rows = cursor.fetchall()

    conn.close()

    movies = []

    for row in rows:
        movies.append(Movie(*row))

    return movies


# --------------------------
# Binary Search
# --------------------------

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid].movie_id == target:
            return arr[mid]

        elif arr[mid].movie_id < target:
            left = mid + 1

        else:
            right = mid - 1

    return None


# --------------------------
# Top 10 Movies
# --------------------------

def top_movies(arr):

    print("\nTop Rated Movies\n")

    sorted_movies = sorted(arr,
                           key=lambda x: x.rating,
                           reverse=True)

    for movie in sorted_movies[:10]:
        movie.display()


# --------------------------
# Most Watched Movie
# --------------------------

def most_watched(arr):

    print("\nMost Watched Movie in Every Genre\n")

    genre_dict = {}

    for movie in arr:

        if movie.genre not in genre_dict:
            genre_dict[movie.genre] = movie

        elif movie.watch_count > genre_dict[movie.genre].watch_count:
            genre_dict[movie.genre] = movie

    for movie in genre_dict.values():
        movie.display()


# --------------------------
# Main Program
# --------------------------

movies = fetch_movies()

# Sort by Rating

movies.sort(key=lambda x: x.rating)

print("Movies Sorted by Rating\n")

for movie in movies:
    movie.display()

# Binary Search

movies.sort(key=lambda x: x.movie_id)

mid = int(input("\nEnter Movie ID to Search: "))

result = binary_search(movies, mid)

if result:
    print("\nMovie Found")
    result.display()
else:
    print("Movie Not Found")

# Top 10

top_movies(movies)

# Most Watched

most_watched(movies)