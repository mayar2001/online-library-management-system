import User
from User import *
from Student import Student as st
import Librarian
from Librarian import *
import Book
from Book import *
import Transaction
from Transaction import *
import Library
from Library import *

# Create some objects like  users , books and transactions and add them to library object
book_1 = Book ('atomic habits' , 'john' ,'science' , 2009)
book_2 = Book ('intro cs' , 'mike' ,'cs' , 2010)
book_3 = Book ('Egypt' , 'tom' ,'history' , 2000)
user_1 = Librarian('john',123 , 'john@gmail.com' , 555 , 'hr')
user_2 = st('joe',456,'joe@gmail.com','python' )
trans_1 = Transaction (user_1 , book_1 , 'return')
trans_2 = Transaction (user_2 , book_2 , 'borrow')

# Create a library by the class 
the_library = Library ('Alex Library')
# Add some objects to the library
the_library.add_book(book_1)
the_library.add_book(book_2)
the_library.add_book(book_3)
the_library.add_user(user_1)
the_library.add_user(user_2)
the_library.add_transaction(trans_1)
the_library.add_transaction(trans_2)
#######the_library.display_library_info()#########################################

print ('Welcome to Alex Library \nIf you are a librarian press 1 .\nIf you are a student press 2 .\nIf you wanna exit press 0')
lib_std_choice = int(input())   
if lib_std_choice == 1 :
    print('If you want to Register press 1.\nIf you want to log in press 2 ')
    reg_log_lib_choice = int(input())
    if reg_log_lib_choice == 1 :
        print('enter your user name')
        userName = input()
        print('enter your password')
        password = int(input())
        print('enter your email')
        email = input()
        print('enter your staff_id')
        staff_id = int(input())
        print('enter your role')
        role = input()
        new_librarian = Librarian(userName,password,email,staff_id,role)
        the_library.add_user(new_librarian)
        search_id = len(the_library.users_list) - 1 
        print ( 'your search id = ',search_id)
        
    elif reg_log_lib_choice == 2 :
        print('Enter your search id ')
        search_id = int(input())
        print('Enter your user name ')
        userName = input()
        print('Enter your password ')
        password = int(input())
        the_librarian = the_library.users_list[search_id]
        if( the_librarian.login(userName , password) ):
            c =0 
            while (c==0):
                print('What do you want to do choose a number\n1-  Update your profile\n2-  Display library info\n3-  Add a Book')
                print('4-  Remove a Book\n5-  Add an User\n6-  Remove an User\n7-  Add a Transaction\n8-  Remove a Transaction')
                print('9-  Display an user info\n10- Update book availability')
                the_option  = int(input())
                
                if the_option == 1:
                    the_librarian.Update()
                    the_librarian.display_user_info(the_librarian)
                
                elif the_option == 2 :
                    the_library.display_library_info()
                
                elif the_option == 3 :
                    # first create an object that carry this book then add it in library list
                    new_book = the_librarian.AddBook()
                    the_library.add_book(new_book)
                    search_book_id = len(the_library.books_list)-1
                    print ('your book search id = ' ,search_book_id)
                    the_library.display_library_info()

                elif the_option == 4 :
                    print('enter book search id ')
                    search_book_id = int(input())
                    the_book = the_library.books_list[search_book_id]
                    the_library.remove_book(the_book)
                    the_librarian.RemoveBook(the_book)
                    the_library.display_library_info()
                
                elif the_option == 5 :
                    # create a user then add it into library list
                    print('enter your user name')
                    userName = input()
                    print('enter your password')
                    password = int(input())
                    print('enter your email')
                    email = input()
                    print('enter your borrowed book list')
                    borrow_list = input()
                    new_user = User(userName,password,email,borrow_list)
                    the_library.add_user(new_user)
                    search_user_id = len(the_library.users_list)-1
                    print('your search user id = ',search_user_id)
                    the_library.display_library_info()
                
                elif the_option == 6 :
                    print('enter user search id ')
                    search_user_id = int(input())
                    the_user = the_library.users_list[search_user_id]
                    the_library.remove_user(the_user)
                    del the_user
                    the_library.display_library_info()
                     
                elif the_option == 7 :
                    # create a transaction then add it into library list
                    print('enter your  search user id')
                    search_user_id = int(input())
                    the_user = the_library.users_list[search_user_id]
                    print('enter your search book id')
                    search_book_id = int(input())
                    the_book = the_library.books_list[search_book_id]
                    print('enter your transaction type ')
                    trans_type = input()
                    new_transaction = Transaction(the_user,the_book,trans_type)
                    the_library.add_transaction(new_transaction)
                    search_trans_id = len(the_library.transactions_list)-1
                    print('your search user id = ',search_trans_id)
                    the_library.display_library_info()
                
                elif the_option == 8 :
                    print('enter  search trans id ')
                    search_trans_id = int(input())
                    the_trans = the_library.transactions_list[search_trans_id]
                    the_library.remove_transaction(the_trans)
                    del the_trans
                    the_library.display_library_info()
                
                elif the_option == 9 : 
                    print('enter user search id ')
                    search_user_id = int(input())
                    the_user = the_library.users_list[search_user_id]
                    the_librarian.display_user_info(the_user)
                
                elif the_option == 10 :
                    print('enter book search id ')
                    search_book_id = int(input())
                    print ('enter the status')
                    status = int(input())
                    the_book = the_library.books_list[search_book_id]
                    if status == 0 :
                      the_librarian.UpdateBookAvailability(the_book , False)
                    elif status == 1 :
                     the_librarian.UpdateBookAvailability(the_book , True)
                    the_book.display_info()
                else:
                    print('enter a valid number')
                
                print('If you want another option Press 0 :')
                Continue = int(input())
                
                c = Continue




elif lib_std_choice == 2 :
    print('If you want to Register press 1.\nIf you want to log in press 2 ')
    reg_log_lib_choice = int(input())
    if reg_log_lib_choice == 1 :
        print('enter your user name')
        userName = input()
        print('enter your password')
        password = int(input())
        print('enter your email')
        email = input()
        print('enter your course')
        course = input()
        new_student = Student(userName,password,email,course)
        the_library.add_user(new_student)
        search_id = len(the_library.users_list) - 1 
        print ( 'your search id = ',search_id)
        
    elif reg_log_lib_choice == 2 :
        print('Enter your search id ')
        search_id = int(input())
        print('Enter your user name ')
        userName = input()
        print('Enter your password ')
        password = int(input())
        the_student = the_library.users_list[search_id]
        if( the_student.login(userName , password) ):
            c = 0
            while(c==0):
                print('What do you want to do choose a number\n1-  Update your profile\n2-  Borrow a book')
                print('3-  Return a book\n4-  View borrowed books')
                the_option = int(input())
            
                if the_option == 1 :
                    #print(the_student.user_name)
                    the_student.Update()
                    #print(the_student.user_name)
                
                elif the_option == 2 :
                    #choose a book ,make a transaction, append to student borrowed book list then add this transaction to library list
                    print('enter search book id')
                    search_book_id = int(input())
                    the_book = the_library.books_list[search_book_id]
                    new_transaction = Transaction(the_student , the_book , 'borrow')
                    the_student.borrow_A_Book(the_book)
                    the_library.add_transaction(new_transaction)
               
                    new_transaction.view_transaction_history()
                    the_student.view_borrowed_books()

                elif the_option == 3 :
                    #choose a book ,make a transaction, remove book  from student borrowed book list then add this transaction to library list
                    print('enter search book id')
                    search_book_id = int(input())
                    the_book = the_library.books_list[search_book_id]
                    new_transaction = Transaction(the_student , the_book , 'return')
                    the_student.return_A_Book(the_book)
                    the_library.add_transaction(new_transaction)
               
                    new_transaction.view_transaction_history()
                    the_student.view_borrowed_books()
    
                elif the_option == 4 :
                    the_student.view_borrowed_books()
                
                else :
                    print('enter a valid number')
                    
                print('if you want another option press 0 : ')
                Continue = int(input())
                
                c = Continue
            
else :
    print ('not valid choice')



























