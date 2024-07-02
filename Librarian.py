from pickle import FALSE
import Book
from Book import *
import User
from User import *

class Librarian(User):
    
    def __init__(self , userName , password , email  , staffId , Role):
        super().__init__(userName, password, email)
        self. Staff_ID = staffId
        self.role = Role


    def AddBook(self ):
        print ('enter the title')
        title=input()
        print ('enter the author')
        author = input()
        print ('enter genre')
        genre = input()
        print ('enter publication year')
        publication_year = input()
        
        book_object = Book (title, author, genre, publication_year)
        return book_object
        
        
    def RemoveBook(self , book_object):
        del book_object
        
    def display_user_info (self , user_object):
        print ('User_id : ' , user_object.user_id ,
               '\nUser_name : ' , user_object.user_name ,
               '\nUser_email :' , user_object.email ,
               '\nUser_borrow_book : ' ) 
        for i in (user_object.borrowedBooks): print (i.title) 
            
    def UpdateBookAvailability(self , book_object , the_status):
        book_object.update_availability( the_status)
 
# book_1 = Book ('atomic habits' , 'john' ,'science' , 2009) 
# user_1 = User('john',123 , 'john@gmail.com' , [book_1])        
# libr_1 =Librarian ('john' , 123 , 'john@gmail.com',555,'HR' ) 

# #book_2 = libr_1.AddBook()
# #book_2.display_info()

# #libr_1.RemoveBook (book_2)
# libr_1.display_user_info(user_1)
# #libr_1.UpdateBookAvailability(book_1 , False)
# #book_1.display_info()






