# test_watchlist.py

from movie import Movie
from watchlist import Watchlist

m1 = Movie("Inception", "Christopher Nolan", 148, 2010)
m2 = Movie("The Godfather", "Francis Ford Coppola", 175, 1972)
m3 = Movie("Interstellar", "Christopher Nolan", 169, 2014)

wl = Watchlist()
wl.add_movie(m1)
wl.add_movie(m2)
wl.add_movie(m3)

wl.show_all()

print("\n🎬 Long movies:")
# print(wl.long_movies()) # shows the item location or the list's location, we need to parse it
# as I was returning all the movie objects in a list, this I was seeing the objects locations

for mov in wl.long_movies():
    print(mov.info())

print("\n⏱️ Total watch time:", wl.total_watch_time())

print("\n🎥 Movies by Christopher Nolan:")
for mov in wl.filter_by_director("Christopher Nolan"):
    print(mov.info())