import User
from User import *
import Transaction
from Transaction import *
import Book
from Book import *

class Student(User):
    def __init__(self, userName , password , email ,  course):
        super().__init__(userName, password, email)
        self.course = course
        self.borrowedBooks = []
        
    
    def borrow_A_Book (self , book):
       self.borrowedBooks.append(book)
        
    def return_A_Book (self , book):
        self.borrowedBooks.remove(book)
        
    # viewing borrowed books
    def view_borrowed_books(self):
         for i in  self.borrowedBooks:
             i.display_info()

#book_1 = Book ('atomic habits' , 'john' ,'science' , 2009)
#book_2 = Book ('intro cs','mike' , 'cs' , 2010)
#std_1 = Student('john',123,'john@gmail.com',[book_1,book_2] , 'python' )
#std_1.view_borrowed_books()








