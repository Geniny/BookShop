import user
import book
import author
import basket
import discount
import tkinter as tk
import appSettings

from tkinter import ttk
from pages import *



set = appSettings.Settings
discount1 = discount.Discount("NONE")

container = None
buttonframe = None
mainBook = None
#authors
author1 = author.Author("Kristie", "Roaling", 1, (2000, 13, 14))
author2 = author.Author("Din", "Bay", 2, (2000, 13, 14))

# books
book1 = book.Book("Harry Potter", 300, 8888,50, "Fantasy", "BelPechat",author1, False , "res/ava1.gif")
book2 = book.Book("Barry Potter P2", 400, 8889,100, "Fantasy", "BelPechat", author1, False, "res/ava3.png")
book3 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")
book4 = book.Book("Aiter Pan P2", 390, 1111,99, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")
book5 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")
book6 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")
book7 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")
book8 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")
book9 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")
book10 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False, "res/hpGF.png")



#users
basket1 = basket.Basket()
user1 = user.User("admin","admin",discount1.userDiscount, basket1, "ivan.petr@mail.ru" , "Ivan Petrov" , "res/ava.gif")

#local base
booksCollection = [book1,book2,book3,book4 , book5,book6,book7,book8,book9,book10]
booksCollection.sort(key = lambda i: i.name )
searchCollection = booksCollection
authenticated = False

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        mainPage = MainPage(self)

        global buttonframe
        global container
        buttonframe , container = mainPage.show()
        buttonframe.place(x = 0 , y = 0 , width = 1280, height = 40)
        container.place(x = 0 , y = 40 , width = 1280 , height = 680)





if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1280x720")
    root.resizable(False, False)
    root.mainloop()

