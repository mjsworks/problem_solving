# book.py
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def summary(self):
        print(f"[{self.title}] by [{self.author}], [{self.pages}] pages.")
    
    def is_long(self):
        # print("Is the book Long?",)
        # print("True" if self.pages>300 else "False")
        return self.pages>300
    
    def read_time(self, word_per_minute):
        return(250*self.pages/word_per_minute)
