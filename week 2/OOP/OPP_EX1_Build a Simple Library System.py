class Book: 
    def __init__(self,title, author):
        self.title =title
        self.author = author
        self.available = True
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Member: 
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed = []
    def __str__(self):
        return f"{self.name} {self.member_id}"

class Library:
    def __init__(self):
        self.books =[]
        self.members =[] 

#Methods add book
    def add_book(self, book):
        self.books.append(book)

#Methods register member
    def register_member(self, member):
        self.members.append(member)

#Methods lend book
    def lend_book(self,book,member):
        if  book.available:
            book.available = False
            member.borrowed.append(book)
            print(f"{book.title} has been lent")
        else: 
             print(f"{book.title} is not abailable for lending")

#Methods lend book
    def return_book(self,book,member):
        if book in member.borrowed :
           book.available = True
           member.borrowed.remove(book)
           print(f" {member.name} have retured {book.title}")
        else:
             print(f" {member.name} do not have borrow {book.title}")
# Example usage:
# Create books
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
# Create members
member1 = Member("John", 101)
member2 = Member("Alice", 102)
# Create library
library = Library()
# Add books to the library
library.add_book(book1)
library.add_book(book2)
# Register members
library.register_member(member1)
library.register_member(member2)

library.lend_book(book1, member1)
library.return_book(book2, member2)