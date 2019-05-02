import tkinter as tk
from tkinter import ttk , PhotoImage
from main import user1 , authenticated , buttonframe , container
from PIL import ImageTk , Image

class Page(tk.Frame):
    def __init__(self, toolbar , container):
        tk.Frame.__init__(self)
        self.toolbar = toolbar
        self.container = container
    def show(self):
        return self.toolbar , self.container

class LoginPage(Page):
    def __init__(self, *args, **kwargs):
        self.toolbar = tk.Frame(bg="orange")
        self.container = tk.Frame(bg="white")

        back_btn = tk.Button(self.toolbar, text='Back',command = self.init_back, bg='white', bd=1, compound=tk.TOP,
                               width=15 )
        label1 = tk.Label(self.container , text = 'Login' , bg = 'orange')
        label2 = tk.Label(self.container , text = 'Password', bg = 'orange')
        self.entry1 = ttk.Entry(self.container)
        self.entry2 = ttk.Entry(self.container)
        login_btn = tk.Button(self.container ,command = self.init_authentication, text = "Login" )

        login_btn.place(x = 640 - 150 , y = 720 / 2 + 31 - 40 + 90 , width = 300 , height = 40)
        back_btn.place(x = 1 , y = 1 , height = 38, width = 100)
        label1.place(x = 640 - 150  , y = 720 / 2 - 70 - 40 , width = 300, height = 40)
        label2.place(x=640 - 150, y=720 / 2 + 31 - 40, width=300, height=40)
        self.entry1.place(x=640 - 100, y=720 / 2 - 30 - 40, width=200, height=40)
        self.entry2.place(x=640 - 100, y=720 / 2 + 71 - 40, width=200, height=40)

        Page.__init__(self, self.toolbar, self.container)

    def init_back(self):
        mainP = MainPage(self)
        global buttonframe
        global container
        buttonframe, container = mainP.show()
        buttonframe.place(x=0, y=0, width=1280, height = 40)
        container.place(x=0, y = 40 ,  width=1280, height=680)

    def init_authentication(self):
        login = self.entry1.get()
        password = self.entry2.get()
        if(user1.login == login and user1.password == password):
            global authenticated
            authenticated = True
            mainPage = MainPage(self)
            global buttonframe
            global container
            buttonframe, container = mainPage.show()
            buttonframe.place(x=0, y=0, width=1280, height=40)
            container.place(x=0, y=40, width=1280, height=680)

class UserPage(Page):
    def __init__(self, *args, **kwargs):
        self.toolbar = tk.Frame(bg="orange")
        self.container = tk.Frame(bg="white")



        tree = ttk.Treeview(self.container)
        tree['columns'] = ('A')
        tree.column('A', width = 250 , minwidth = 250)
        tree.column('#0' , width = 250 , minwidth = 250)
        tree.heading("#0", text = "Book")
        tree.heading("A" , text = "Author")

        image = Image.open("res/ava.gif")
        avatar = ImageTk.PhotoImage(image)
        back_btn = tk.Button(self.toolbar, text='Back', command=self.init_back, bg='white', bd=1, compound=tk.TOP, width=15)
        label = tk.Label(self.container,image = avatar )
        label.image = avatar
        birth_lbl = tk.Label(self.container , text = "Birthdate: {}".format(user1.birthdate) , font=("Helvetica", 16) , justify = tk.LEFT , anchor = tk.W)
        user_lbl = tk.Label(self.container , text = "User info" , font=("Helvetica", 16))

        back_btn.place(x = 1 , y = 1 , height = 38, width = 100)
        tree.place(x = 780 , y = 1, height = 680 , width = 500)
        label.place(x = 1 , y = 1 , height = 300 , width = 300)
        birth_lbl.place(x = 303 , y = 42 , height = 40 , width = 300)
        user_lbl.place(x = (1280 - 500+300)/2 - 150 , y = 1,height = 40 , width = 300)

        Page.__init__(self, self.toolbar, self.container)

    def init_back(self):
        mainPage = MainPage(self)
        global buttonframe
        global container
        buttonframe, container = mainPage.show()
        buttonframe.place(x=0, y=0, width=1280, height = 40)
        container.place(x=0, y = 40 ,  width=1280, height=680)

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
        container.place(x=0, y=40, width=1280, height=680)

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
        user_btn = tk.Button(self.toolbar, text='User info', bg='white', command=self.init_User, bd=1, compound=tk.TOP,
                              width=15)
        basket_btn = tk.Button(self.toolbar, text='Basket', bg='white', command=self.init_Basket, bd=1, compound=tk.TOP,
                              width=15)
        search_btn = tk.Button(self.toolbar, text='Search', bg='white', command=self.init_Login, bd=1, compound=tk.TOP,
                               width=15)
        search = ttk.Entry(self.toolbar)

        search.place(x = 300 , y = 1 , height = 38, width = 869)
        global authenticated
        if authenticated:
            user_btn.place(x=1, y=1, height=38, width=100)
        else:
            login_btn.place(x=1, y=1, height=38, width=100)
        basket_btn.place(x=199, y=1, height=38, width=100)
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
        container.place(x=0, y = 40, width=1280, height=680)

    def init_Basket(self):
        basketPage = BasketPage(self)
        global buttonframe
        global container
        buttonframe, container = basketPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)

    def init_User(self):
        userPage = UserPage(self)
        global buttonframe
        global container
        buttonframe, container = userPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)
