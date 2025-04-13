# bookshelf.py
from book import Book

class Bookshelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def total_pages(self):
        return sum(book.pages for book in self.books)
    
    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

    def long_books(self):
        for book in self.books:
            if book.is_long():
                print(f"{book.title} is a long book!")
    
    def avg_read_time(self, word_per_minute):
        total_time = sum(book.read_time(word_per_minute) for book in self.books)
        return total_time/len(self.books) if self.books else 0