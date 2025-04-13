from book import Book
from bookshelf import Bookshelf

b1 = Book("Atomic Habits", "James Clear", 320)
b2 = Book("The Alchemist", "Paulo Coelho", 280)
b3 = Book("Deep Work", "Cal Newport", 304)

shelf = Bookshelf()
shelf.add_book(b1)
shelf.add_book(b2)
shelf.add_book(b3)

print("📘 All books on shelf:")
shelf.show_books()

print("\n📖 Total pages:", shelf.total_pages())

print("\n📏 Long books:")
shelf.long_books()

print(f"\n⏱️ Average read time at 70 wpm: {shelf.avg_read_time(70):.2f} minutes")