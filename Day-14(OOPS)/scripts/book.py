# 1. Create a Book class with title, author, and pages attributes. Add a __str__() method to print nicely.
class Book:
    
    def __init__(self,title,author,pages):
        self.title  = title
        self.author = author
        self.pages  = pages
        
    def __str__(self):
        return f'Book : {self.title} by {self.author}, {self.pages} pages'