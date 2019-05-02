import user
import book
import author
import basket
import tkinter as tk
from tkinter import ttk

import appSettings

set = appSettings.Settings


container = None
buttonframe = None
#authors
author1 = author.Author("Kristie", "Roaling", 1, (2000, 13, 14))
author2 = author.Author("Din", "Bay", 2, (2000, 13, 14))

# books
book1 = book.Book("Harry Potter", 300, 8888,50, "Fantasy", "BelPechat",author1, False)
book2 = book.Book("Barry Potter P2", 400, 8889,100, "Fantasy", "BelPechat", author1, False)
book3 = book.Book("Piter Pan", 210, 1111,200, "Fantasy", "RusPechat",author2, False)
book4 = book.Book("Aiter Pan P2", 390, 1111,99, "Fantasy", "RusPechat",author2, False)

#users
basket1 = basket.Basket()
user1 = user.User("admin","admin",None, basket1)

#local base
booksCollection = [book1,book2,book3,book4]
booksCollection.sort(key = lambda i: i.name )
global authenticated
authenticated = False

def menu(authenticated):
    print("\nMain menu")
    print("   1. Show books")
    print("   2. Find book ")
    if authenticated:
        print("   3. Show user info")
        print("   4. Show purchaces")
        print("   5. Exit from programm")
    else:
        print("   3. Log in")
        print("   4. Exit from programm")

    while(True):
         try:
            switch = input()
         except:
             switch = input()
         if switch == '1':
             showBooks()
         elif switch == '2':
             searchBook()
         elif switch == '3':
             if authenticated:
                 userInfo()
             else:
                 authenticated = authentication()
                 menu(authenticated)
         elif switch == '4':
             if authenticated:
                showBasket()
             else:
                 return
         elif switch == '5':
             return

def showBooks():
    count = len(booksCollection)
    print("Book collection ")
    for i in range(0,count):
        print("   {}. {}".format(i+1,booksCollection[i].name))
    print("   {}. Back".format(count + 1))
    while(True):
        switch = int(input())
        if (switch >= 1) and (switch <= count):
            switch -= 1
            bookInfo(switch)
            break
        elif switch == count + 1:
            menu(authenticated)

def bookInfo(switch):
    print("\nBook info")
    print("   Book name: {}\n   "
          "Ganre: {}\n   "
          "Pages: {}\n   "
          "Cost: {}\n   "
          "Publisher: {}\n".format(booksCollection[switch].name,
                              booksCollection[switch].ganre,
                              booksCollection[switch].pages,
                              booksCollection[switch].cost,
                              booksCollection[switch].pname))
    print("   1. Add in a basket")
    print("   2. Show author info")
    print("   3. Back")
    switch = int(input())
    if switch == 3:
        showBooks()
    elif switch == 1:
        addInBasket(switch)
    elif switch == 2:
        authorInfo(switch)

def authorInfo(switch):
    print("\nAuthor info")
    print("   Author name: {}\n"
          "   Birthdate: {}\n"
          "   Rank: {}\n".format(booksCollection[switch].author.name +" "+ booksCollection[switch].author.surname,
                       booksCollection[switch].author.birthdate,booksCollection[switch].author.rank))
    print("   1. Back")
    if int(input()) == 1:
        bookInfo(switch)

def searchBook():
    print("Enter name: ", end ='')
    string = str(input())
    searchedBooks = []
    for i in booksCollection:
        if(string in i.name):
            searchedBooks.append(i)
    for i in range(0,len(searchedBooks)):
        print("   {}.{}".format(i+1,searchedBooks[i].name))

    if int(input()) == 1:
        menu(authenticated)

def addInBasket(switch):
    if authenticated:
        if  booksCollection[switch].purchased == False:
            booksCollection[switch].purchased = True
        else:
            print("Book already purchased")
        basket1.__add__(booksCollection[switch])
        print("Purchase complete , press 1 to back")
        if int(input()) == 1:
            menu(authenticated)
    else:
        print("Log in ")
        menu(authenticated)

def showBasket():
    print("User purchase basket")
    if basket1.purchases != None:
        for i in basket1.purchases:
            print("   {}".format(i.name))
        print("\n   1. Purchase all")
        print("   2. Back")
        while(True):
            temp = int(input())
            if temp == 1:
                for i in basket1.purchases:
                    user1.deposit -= i.cost
                    user1.purchaseList.append(i)
                if user1.deposit > 0:
                    basket1.purchases = None
                else:
                    print("Not enough money")
                menu(authenticated)
            if temp == 2:
                menu(authenticated)
    else:
        print("There are no books")
        print("\n   1. Back")
        if int(input()) == 1:
            menu(authenticated)

def userInfo():
    print("\nUser info:")
    print("   Login: ", user1.login)
    print("   Deposit: ",user1.deposit)
    print("\nPurchase list:")
    for i in user1.purchaseList:
        print("   {}".format(i.name))
    if int(input()) == 1:
        menu(authenticated)

def authentication():
    print("Enter login: ", end= '')
    login = str(input())
    while(True):
        print("Enter password: ",end='')
        password = str(input())
        if(password == user1.password):
             global authenticated
             authenticated = True
             menu(authenticated)
        elif password == '0':
            return False
        else:
            print("Password not correct")

class Page(tk.Frame):
    def __init__(self, toolbar , container):
        tk.Frame.__init__(self)
        self.toolbar = toolbar
        self.container = container
    def show(self):
        return self.toolbar , self.container


class BasketPage(Page):
    def __init__(self, *args, **kwargs):
        self.toolbar = tk.Frame(bg="blue")
        self.container = tk.Frame(bg="brown")
        back_btn = tk.Button(self.toolbar, text='Back', command=self.init_back, bg='white', bd=1, compound=tk.TOP,
                             width=15)

        back_btn.place(x=1, y=1, height=38, width=100)
        Page.__init__(self, self.toolbar, self.container)

    def init_back(self):
        mainPage = MainPage(self)

        global buttonframe
        global container
        buttonframe, container = mainPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=500)


class LoginPage(Page):
    def __init__(self, *args, **kwargs):
        self.toolbar = tk.Frame(bg="blue")
        self.container = tk.Frame(bg="brown")
        back_btn = tk.Button(self.toolbar, text='Back',command = self.init_back, bg='white', bd=1, compound=tk.TOP,
                               width=15 )
        label1 = tk.Label(self.container , text = 'Login')
        label2 = tk.Label(self.container , text = 'Password')
        entry1 = ttk.Entry(self.container)
        entry2 = ttk.Entry(self.container)

        back_btn.place(x = 1 , y = 1 , height = 38, width = 100)
        label1.place(x = 640 - 80  , y = 720 / 2 - 60 , width = 150, height = 30)
        label2.place(x=640 - 80, y=720 / 2 + 60, width=150, height=30)
        Entry1.place(x=640 - 80, y=720 / 2 - 30, width=150, height=30)
        entry2.place(x=640 - 80, y=720 / 2 + 30, width=150, height=30)

        Page.__init__(self, self.toolbar, self.container)

    def init_back(self):
        mainPage = MainPage(self)

        global buttonframe
        global container
        buttonframe, container = mainPage.show()
        buttonframe.place(x=0, y=0, width=1280, height = 40)
        container.place(x=0, y = 40 ,  width=1280, height=500)

class BookPage(Page):
    def __init__(self, *args, **kwargs):
        self.toolbar = tk.Frame(bg="green")
        self.container = tk.Frame(bg="yellow")
        label = tk.Label(self.toolbar, text="Book page")
        label.pack()
        Page.__init__(self, self.toolbar, self.container)

class MainPage(Page):
    def __init__(self, *args, **kwargs):
        self.toolbar = tk.Frame(bg = "orange")
        self.container = tk.Frame(bg = "red")


        treeCat = ttk.Treeview(self.container)
        treeCat.heading('#0', text = 'Categories')

        treeBooks = ttk.Treeview(self.container)
        treeBooks["columns"]=('books')
        treeBooks.column('#0', width = 250 , minwidth = 250, stretch = tk.NO)
        treeBooks.column('books', width=750, minwidth = 750, stretch=tk.NO)
        treeBooks.heading('#0', text = "Book", anchor = 'center')
        treeBooks.heading('books' , text = "Book info", anchor = 'center')

        login_btn = tk.Button(self.toolbar, text='Login', bg='white', command=self.init_Login, bd=1, compound=tk.TOP,
                              width=15)
        basket_btn = tk.Button(self.toolbar, text='Basket', bg='white', command=self.init_Login, bd=1, compound=tk.TOP,
                              width=15)
        search_btn = tk.Button(self.toolbar, text='Search', bg='white', command=self.init_Login, bd=1, compound=tk.TOP,
                               width=15)
        search = ttk.Entry(self.toolbar)

        search.place(x = 318 , y = 1 , height = 38, width = 850)
        login_btn.place(x=1, y=1, height=38, width=100)
        basket_btn.place(x=106, y=1, height=38, width=100)
        search_btn.place(x=1174, y=1, height=38, width=105)
        treeCat.place(x = 0 , y = 0 , height = 680 , width = 300)
        treeBooks.place(x = 300 , y = 0 , width = 980 , height = 680)

        Page.__init__(self, self.toolbar, self.container)

    def init_Login(self):
        loginPage = LoginPage(self)
        global buttonframe
        global container
        buttonframe, container = loginPage.show()
        buttonframe.place(x=0, y = 0, width=1280, height = 40)
        container.place(x=0, y = 40, width=1280, height=500)

    def init_Basket(self):
        basketPage = BasketPage(self)
        global buttonframe
        global container
        buttonframe, container = loginPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=500)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        mainPage = MainPage(self)

        global buttonframe
        global container
        buttonframe , container = mainPage.show()
        buttonframe.place(x = 0 , y = 0 , width = 1280, height = 40)
        container.place(x = 0 , y = 40 , width = 1280 , height = 500)





if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1280x720")
    root.mainloop()

