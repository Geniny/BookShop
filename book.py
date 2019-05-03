import author
from PIL import Image , ImageTk

class Book:
    __doc__ = "Book class"

    def __init__(self , name: str, pages: int, isbn: int,cost: int, ganre: str, pname: str, author: author, purchased: bool , imagepath: str):
        self.image = Image.open(imagepath)
        self.name = name
        self.pages = pages
        self.isbn = isbn
        self.ganre = ganre
        self.pname = pname
        self.cost = cost
        self.author = author
        self.purchased = purchased

