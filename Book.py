class Book:
     
    def __init__(self, title, author, genre, publication_year):
        self.book_id = id(self)
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.availability = True

    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Availability: {'Available' if self.availability else 'Not Available'}")

    def update_availability(self, status):
        self.availability = status
        
#book_1 = Book ('atomic habits' , 'john' ,'science' , 2009)
#book_1.display_info()
#book_1.update_availability(False)
#book_1.display_info()