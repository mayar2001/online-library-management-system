
import Book
from Book import *

class User:
    
#   register new user 
    def __init__(self , userName , password , email ):
        self.user_id = id(self)
        self.user_name = userName 
        self.password = password
        self.email = email
    

    def login(self , userName , password ):
        if self.user_name == userName and self.password == password :
            return True
        else:
            print ('something wrong retry login')
            
    def Update(self):
        print('If you want to update your username enter 1')
        print('If you want to update your password enter 2')
        choice = int(input(print('If you want to update your email enter 3: ')))
        if choice == 1:
            new_username = input('Enter your new username')
            self.user_name = new_username
            
        elif choice == 2:
            new_password= input('Enter your new password')
            self.password = new_password
            
        elif choice == 3:
            new_email = input('Enter your new email')
            self.email = new_email
            
        else:
            print('Wrong choise')
            
          
#book_1 = Book ('atomic habits' , 'john' ,'science' , 2009) 
#user_1 = User('john',123 , 'john@gmail.com' , [book_1])
#user_1.login('john' , 256)
#user_1.login('john' , 123)
#user_1.Update()




