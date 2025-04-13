# watchlist.py

from movie import Movie

class Watchlist:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
    
    def show_all(self):
        for movie in self.movies:
            print(f"title -> {movie.title}, Year -> {movie.year}")
    
    def long_movies(self):
        return [movie for movie in self.movies if movie.is_long()]
    
    def total_watch_time(self):
        return sum(movie.duration for movie in self.movies)
    
    def filter_by_director(self, director):
        return [movie for movie in self.movies if movie.director==director]
            