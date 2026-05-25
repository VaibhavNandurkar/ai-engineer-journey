class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author
        self.is_available = True
    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f'"{self.title}" by {self.author} [{status}]'
    
class Member:
    def __init__(self, name ,member_id):  
        self.name  = name 
        self.memeber_id = member_id
        self.borrowed_books = []
    def __str__(self):
        return f"{self.name} (ID: {self.memeber_id}) - {len(self.borrowed_books)} book(s) borrowed" 
    def borrow(self, book):
        if book.is_available:
           book.is_available = False
           self.borrowed_books.append(book)
           print(f"{self.name} borroweed {book.title}")
        else:
           print(f"{book.title} is not available right now")  
    def return_book(self, book):
        if book in self.borrowed_books:
            book._is_available  = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

class Library:
    def __init__(self, name):
        self.name = name 
        self.books = []
        self.members = []
    def add_book(self, book):
        self.books.append(book)
        print(f'Added "{book.title}" to {self.name}')      
    def add_member(self, member):
        self.members.append(member)   
        print(f'Registered member: {self.members}')
    def show_available_books(self):
        print(f'\nAvailable books at {self.name}:') 
        available = [b for b in self.books if b.is_available]
        if available:
            for b in available:
                print(f"  {b}")
        else:
            print("  No books available right now")

lib = Library("City Library")                          

b1 = Book("Atomic Habits", "James Clear")
b2 = Book("Deep Work", "Cal Newport")
b3 = Book("The Pragmatic Programmer", "Hunt & Thomas")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
m1 = Member("Vaibhav", "M001")
m2 = Member("Anjali", "M002")
lib.add_member(m1)
lib.add_member(m2)

lib.show_available_books()
m1.borrow(b1)
m2.borrow(b2)

lib.show_available_books()
m1.return_book(b1)

lib.show_available_books()



print(b1)
print(b2)
print(m1)
print(m2)