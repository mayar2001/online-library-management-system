from datetime import datetime
import Book 
from Book import *
import User
from User import *
import Student
from Student import *

class Transaction () :
    def __init__ (self , User , book , transaction_type):
        
        self.transaction_id = id(self)
        self.timestamp = datetime.now()
        self.user = User 
        self.book = book
        self.set_trans_type (transaction_type)

    def check_trans_type (self,trans_type):
        if trans_type == 'borrow' or trans_type == 'return' :
            self.transaction_type = trans_type 
            return 1
        else :
            print ('enter a correct transaction type either "borrow" or "return" only ')
            return 0
    
    def set_trans_type (self,trans_type):
        
        check_unit = self.check_trans_type (trans_type) 
        while (check_unit == 0):
            update_trans_type = input()
            check_unit = self.check_trans_type (update_trans_type)

    def view_transaction_history (self ):
      
            print ('Transaction Id : ' , self.transaction_id ,
                   '\nTime of transaction : ' , self.timestamp ,
                   '\nUser ID : ' , self.user.user_id ,
                   '\nUser Name: ' , self.user.user_name ,
                   '\nBook ID : ' , self.book.book_id ,
                   '\nBook Title: ' , self.book.title ,
                   '\nTransaction type : ' , self.transaction_type )

            
#book_1 = Book ('atomic habits' , 'john' ,'science' , 2009)
#user_1 = User('john',123 , 'john@gmail.com' , [book_1])            
#the_trans = Transaction (user_1 , book_1 , 'return')
#the_trans.view_transaction_history()