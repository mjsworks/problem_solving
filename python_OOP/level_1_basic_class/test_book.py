from book import Book # filename then classname

b1 = Book("Atomic Habits", "James Clear", 320)
b2 = Book("The Alchemist", "Paulo Coelho", 280)

# Call the functions
b1.summary()
print("Is the book long? -> ", b1.is_long())
print(f"time needed to read {b1.title} is: {b1.read_time(60)} minutes")

b2.summary()
print("Is the book long? -> ", b2.is_long())
print(f"time needed to read {b2.title} is: {b2.read_time(70)} minutes")