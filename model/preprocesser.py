import multiprocessing
from user import User
from movie import Movie
from rating import Rating
import time

delimiter = "::"

ratingsFileName = "../data/ratings.dat"
moviesFileName = "../data/movies.dat"
usersFileName = "../data/users.dat"
users = []
ratings = []
movies = []

def readUsers():
    with open(usersFileName, 'r') as usersFile:
        data = usersFile.readlines()
        for line in data:
            userId, gender, age, occupation, zip_code = line.split(delimiter)
            users.append(User(userId, gender, age, occupation, zip_code))

def readMovies():
    with open(moviesFileName, 'r') as moviesFile:
        data = moviesFile.readlines()
        for line in data:
            movieId, title, genres = line.split(delimiter)
            movies.append(Movie(movieId, title, genres))

def readRatings():
    with open(ratingsFileName, 'r') as ratingsFile:
            data = ratingsFile.readlines()
            for line in data:
                userId, movieId, rating, timestamp = line.split(delimiter)
                ratings.append(Rating(userId, movieId, rating, timestamp))

start = time.time()
readUsers() 
readMovies()
readRatings()
end = time.time()
elapsed = end - start
print("Elapsed time: ", elapsed)
