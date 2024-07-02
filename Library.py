import User
from User import * 
import Book
from Book import *
import Transaction
from Transaction import *

class Library:
    def __init__(self, library_name ):
        self.library_name = library_name
        self.books_list = []
        self.users_list = []
        self.transactions_list = []
     
    
    def display_library_info(self):
            print('Library Name: ',self.library_name , 
                  '\nbook list : ',len(self.books_list),' books' )
            for i in self.books_list:
                print('book id: ',i.book_id, ', book title : ' , i.title)  
            print('user list : ',len(self.users_list),' useres' )
            for j in self.users_list :
                print('user id: ',j.user_id , ', user name: ' , j.user_name)  
            print('transaction_list :' ,len(self.transactions_list),' transactions')
            for s in self.transactions_list :
                print('transaction id: ' , s.transaction_id) 
           
            
    def add_book(self, book):
        self.books_list.append(book)
        #print('A Book added to the library.')
   
    def remove_book(self, book):
         
        if book in self.books_list:
                self.books_list.remove(book)
                #print( 'A Book removed from the library')
        else:
             print('Book canot remove this book, not found in the library')
    
    def add_user(self, user):
        self.users_list.append(user)
        #print('User added to the library.')

    def remove_user(self, user):
            
            if user in self.users_list:
                self.users_list.remove(user)
               # print('User removed from the library')
            else:
                print( 'User  not found in the library.')
                
    def add_transaction(self, transaction_id):
        self.transactions_list.append(transaction_id)
        #print("Transaction added to the library.")
    
        
    def remove_transaction(self, transaction):
        
        if transaction in self.transactions_list:
                self.transactions_list.remove(transaction)
                #print('Transactio removed from the library.')
        else:
             print('Transaction  not found in the library.')
                 
        

# book_1 = Book ('atomic habits' , 'john' ,'science' , 2009)
# book_2 = Book ('intro cs' , 'mike' ,'cs' , 2010)

# user_1 = User('john',123 , 'john@gmail.com' , [book_1])


# the_trans = Transaction (user_1 , book_1 , 'return')


# lib_1 = Library ('alex')
# lib_1.display_library_info()
# print('--------------------------------------------------------------')

# lib_1.add_book(book_1)
# lib_1.add_book(book_2)
# lib_1.add_user(user_1)
# lib_1.add_transaction(the_trans)

# lib_1.display_library_info()
# print('------------------------------------------------------------')

# lib_1.remove_book(book_2)
# lib_1.remove_transaction(the_trans)
# lib_1.remove_user(user_1)

# lib_1.display_library_info()



















