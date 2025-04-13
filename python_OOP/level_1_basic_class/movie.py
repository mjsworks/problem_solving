# movie.py

class Movie:
    def __init__(self, title, director, duration, year):
        self.title = title
        self.director = director
        self.duration = duration
        self.year = year
    
    def info(self):
        print(f"{self.title} ({self.year}), directed by {self.director}, {self.duration} minutes")

    def is_long(self):
        return self.duration>150
    
    def is_classic(self):
        return self.year<2000