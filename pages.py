import tkinter as tk
import discount
from tkinter import ttk , PhotoImage
from main import user1 , authenticated , buttonframe , container , booksCollection , mainBook , basket1 , searchCollection
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
                               width=15 , font=("Helvetica", 16))
        label1 = tk.Label(self.container , text = 'Login' , bg = 'orange', font=("Helvetica", 16))
        label2 = tk.Label(self.container , text = 'Password', bg = 'orange', font=("Helvetica", 16))
        self.entry1 = ttk.Entry(self.container)
        self.entry2 = ttk.Entry(self.container)
        login_btn = tk.Button(self.container ,command = self.init_authentication, text = "Login" , font=("Helvetica", 16))

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
        global user1
        if(user1.getCount() >= 3):
            disc = discount.Discount("DEF")
            user1.userDiscount = disc.userDiscount
        style = ttk.Style(self.container)
        style.configure("Treeview", rowheight = 100 , font=("Helvetica", 16), anchor = tk.CENTER , justify = tk.CENTER)
        style.configure("Treeview.Heading", font=("Helvetica", 16))
        self.tree = ttk.Treeview(self.container , column = ("A"))
        self.tree.column('A', width = 250 , minwidth = 250)
        self.tree.column('#0' , width = 250 , minwidth = 250)
        self.tree.heading("#0", text = "Book")
        self.tree.heading("A" , text = "Author")

        avatar = ImageTk.PhotoImage(user1.image)

        back_btn = tk.Button(self.toolbar, text='Back', command=self.init_back, bg='white', bd=1, compound=tk.TOP, width=15, font=("Helvetica", 16))
        label = tk.Label(self.container,image = avatar )
        label.image = avatar
        money_lbl = tk.Label(self.container, text="Money deposit: {}".format(user1.deposit), font=("Helvetica", 16), justify=tk.LEFT,anchor=tk.W , bg = "white")
        city_lbl = tk.Label(self.container , text = "City: {}".format(user1.city) , font=("Helvetica", 16) , justify = tk.LEFT , anchor = tk.W , bg = "white")
        birth_lbl = tk.Label(self.container , text = "Birthdate: {}".format(user1.birthdate) , font=("Helvetica", 16) , justify = tk.LEFT , anchor = tk.W , bg = "white")
        email_lbl = tk.Label(self.container , text = "E-mail: {}".format(user1.email) , font=("Helvetica", 16) , justify = tk.LEFT , anchor = tk.W , bg = "white")
        initials_lbl = tk.Label(self.container , text = "Initials: {}".format(user1.initials) , font=("Helvetica", 16) , justify = tk.LEFT , anchor = tk.W , bg = "white")
        user_lbl = tk.Label(self.container , text = "User info" , font=("Helvetica", 16) , bg = "orange")
        discount_lbl = tk.Label(self.container , text = "Discount: {} %".format(user1.userDiscount) , font=("Helvetica", 16) , justify = tk.LEFT , anchor = tk.W , bg = "white")
        header_lbl = tk.Label(self.toolbar, text="Purchase list", bg="white", anchor="center", bd=1, font=("Helvetica", 16))
        info_lbl = tk.Label(self.container , text = "Books count: {}".format(user1.getCount()) , font=("Helvetica", 16) , bg = "orange")

        for x in user1.purchaseList:
            _img = ImageTk.PhotoImage(x.image, height=100, width=100)
            self.tree.insert('', 'end', text=x.name, image=_img,
                             values=(
                             x.author.name + " " + x.author.surname, x.cost - (user1.userDiscount * x.cost / 100)))
            self.label = tk.Label(self.container, image=_img)
            self.label.image = _img

        header_lbl.place(x=580, y=2, width=698, height=36)
        back_btn.place(x = 1 , y = 1 , height = 38, width = 100)
        self.tree.place(x = 580 , y = 1, height = 640 , width = 700)
        label.place(x = (1280 - 700)/2 - 150 , y = 1 , height = 300 , width = 300)
        initials_lbl.place(x = 1 , y = 372 , height = 40 , width = 300)
        birth_lbl.place(x = 1 , y = 413 , height = 40 , width = 300)
        city_lbl.place(x=1, y=454, height=40, width=300)
        money_lbl.place(x=1, y=495, height=40, width=300)
        discount_lbl.place(x=1, y=536, height=40, width=300)
        email_lbl.place(x=1, y=577, height=40, width=300)
        user_lbl.place(x = (1280 - 700+300)/2 - 300 , y = 311,height = 40 , width = 300)
        info_lbl.place(x = 580 , y = 640 , height = 40 , width = 700)

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
        global authenticated , basket1
        self.toolbar = tk.Frame(bg="orange")
        self.container = tk.Frame(bg="white")
        style = ttk.Style(self.container)
        style.configure("Treeview", rowheight = 100 , font=("Helvetica", 16), anchor = tk.CENTER , justify = tk.CENTER)
        style.configure("Treeview.Heading", font=("Helvetica", 16))



        self.tree = ttk.Treeview(self.container , column = ("#1","#2"))
        self.tree.column('#1', width = 200 , minwidth = 200)
        self.tree.column('#0' , width = 250 , minwidth = 250)
        self.tree.column('#2', width=50, minwidth=50)
        self.tree.heading("#0", text = "Book")
        self.tree.heading("#1" , text = "Author")
        self.tree.heading("#2", text="Cost")
        totalCost = tk.StringVar()
        if basket1 != []:
            for x in basket1.purchases:
                _img = ImageTk.PhotoImage(x.image, height=100, width=100)
                self.tree.insert('', 'end', text=x.name, image=_img,
                                      values=(x.author.name + " " + x.author.surname, x.cost - (user1.userDiscount * x.cost / 100)))
                self.label = tk.Label(self.container, image=_img)
                self.label.image = _img
            totalCost.set("Total cost: {}".format(self.init_totalCost(basket1.purchases)))
        else:
            totalCost.set("Basket is empty")

        back_btn = tk.Button(self.toolbar, text='Back', command=self.init_back, bg='white', bd=1, compound=tk.TOP,
                             width=15, font=("Helvetica", 16))
        header_lbl = tk.Label(self.toolbar, text="Basket", bg="white", anchor="center", bd=1, font=("Helvetica", 16))
        cost_lbl = tk.Label(self.container, textvariable=totalCost, bg="orange", anchor="center", bd=1,
                            font=("Helvetica", 16))
        purch_all_btn = tk.Button(self.container, text="Purchase all", command=self.init_purchase_all, bg='orange',
                                  bd=1, compound=tk.TOP, width=15, font=("Helvetica", 16))
        clear_all_btn = tk.Button(self.container, text="Clear basket", command=self.init_clear_all, bg='orange',
                                  bd=1, compound=tk.TOP, width=15, font=("Helvetica", 16))

        cost_lbl.place(x = 580/2 - 100 , y = 680/2 + 200 , height = 40 , width = 200)
        self.tree.place(x=580, y=1, height=680, width=700)
        header_lbl.place(x = 580, y = 2 , width = 698 , height = 36)
        back_btn.place(x=1, y=1, height=38, width=100)
        purch_all_btn.place(x = 580/2 - 100 , y = 680/2 + 100 , height = 40 , width = 200)
        clear_all_btn.place(x = 580/2 - 100 , y = 680/2 + 59 , height = 40 , width = 200)
        Page.__init__(self, self.toolbar, self.container)

    def init_back(self):
        mainPage = MainPage(self)

        global buttonframe
        global container
        buttonframe, container = mainPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)

    def init_totalCost(self, collection):
        global user1
        sum = 0
        for x in collection:
            sum += x.cost
        return sum - (sum * user1.userDiscount / 100)

    def init_purchase_all(self):
        global  user1 , basket1, booksCollection , buttonframe , container, authenticated

        if authenticated:
            for x in basket1.purchases:
                user1.purchaseList.append(x)
                user1.deposit -= x.cost
                for y in booksCollection:
                    if x.name == y.name:
                        y.purchased = True
                        break


            basket1.purchases = []
            basketPage = BasketPage(self)
            buttonframe, container = basketPage.show()
            buttonframe.place(x=0, y=0, width=1280, height=40)
            container.place(x=0, y=40, width=1280, height=680)

    def init_clear_all(self):
        global user1, basket1, booksCollection, buttonframe, container

        basket1.purchases = []
        basketPage = BasketPage(self)
        buttonframe, container = basketPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)

class BookPage(Page):
    def __init__(self,book , *args, **kwargs):
        self.toolbar = tk.Frame(bg="orange")
        self.container = tk.Frame(bg="white")
        global mainBook , basket1 , container , buttonframe
        buttonText = tk.StringVar("")
        if mainBook.purchased:
            buttonText.set("Already purchased")
        else:
            if basket1.purchases != []:
                for x in basket1.purchases:
                    if x.name == mainBook.name:
                        buttonText.set("Already in basket")
                        break
                    else:
                        buttonText.set("Add in basket")
            else:
                buttonText.set("Add in basket")
        back_btn = tk.Button(self.toolbar, text='Back', command=self.init_back, bg='white', bd=1, compound=tk.TOP, width=15, font=("Helvetica", 16))
        basket_btn = tk.Button(self.container,command=self.init_addInBasket,textvariable = buttonText, bg='orange', bd=1, compound=tk.TOP, width=15, font=("Helvetica", 16))
        header_lbl = tk.Label(self.toolbar, text = "Book info" , bg = "white" , anchor = "center" , bd = 1, font=("Helvetica", 16))
        bname_lbl = tk.Label(self.container, text="Book name: {}".format(mainBook.name), bg="white", anchor=tk.W, bd=1, font=("Helvetica", 16))
        aname_lbl = tk.Label(self.container, text="Author name: {} {}".format(mainBook.author.name, mainBook.author.surname), bg="white", anchor=tk.W, bd=1, font=("Helvetica", 16))
        ganre_lbl = tk.Label(self.container, text="Ganre: {}".format(mainBook.ganre), bg="white",
                             anchor=tk.W, bd=1, font=("Helvetica", 16))
        isbn_lbl = tk.Label(self.container, text="ISBN: {}".format(mainBook.isbn), bg="white",
                             anchor=tk.W, bd=1, font=("Helvetica", 16))
        pname_lbl = tk.Label(self.container, text="Publisher name: {}".format(mainBook.pname), bg="white",
                             anchor=tk.W, bd=1, font=("Helvetica", 16))
        abirth_lbl = tk.Label(self.container, text="Birthdate: {}".format(mainBook.author.birthdate), bg="white",
                             anchor=tk.W, bd=1, font=("Helvetica", 16))
        arank_lbl = tk.Label(self.container, text="Rank: {}".format(mainBook.author.rank), bg="white",
                             anchor=tk.W, bd=1, font=("Helvetica", 16))
        pages_lbl = tk.Label(self.container, text="Pages: {}".format(mainBook.pages), bg="white",
                             anchor=tk.W, bd=1, font=("Helvetica", 16))
        cost_lbl = tk.Label(self.container, text="Cost: {}".format(mainBook.cost - (user1.userDiscount * mainBook.cost / 100)), bg="orange",
                             anchor=tk.CENTER, bd=1, font=("Helvetica", 16))



        back_btn.place(x=1, y=1, height=38, width=100)
        header_lbl.place(x = 580, y = 2 , width = 698 , height = 36)
        bname_lbl.place(x = 580 , y = 81 , width = 700 , height = 40)
        aname_lbl.place(x=580, y=42 + 80, width=700, height=40)
        abirth_lbl.place(x=630, y=83+ 80, width=700, height=40)
        arank_lbl.place(x=630, y=124+ 80, width=700, height=40)
        pname_lbl.place(x=580, y=165+ 80, width=700, height=40)
        isbn_lbl.place(x=580, y=206+ 80, width=700, height=40)
        ganre_lbl.place(x=580, y=247+ 80, width=700, height=40)
        pages_lbl.place(x=580, y=288+ 80, width=700, height=40)
        cost_lbl.place(x = 580, y = 368 + 80 , width = 698 , height = 46)
        basket_btn.place(x = 200, y = 680 / 2, height = 40 , width = 200)

        Page.__init__(self, self.toolbar, self.container)

    def init_back(self):
        global basket1, buttonframe, container, mainBook
        mainPage = MainPage(self)
        buttonframe, container = mainPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)

    def init_addInBasket(self):
        global basket1, buttonframe, container, mainBook
        basket1.__add__(mainBook)
        bookPage = BookPage(self)
        buttonframe, container = bookPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)


class MainPage(Page):
    def __init__(self, *args, **kwargs):
        global searchCollection
        self.toolbar = tk.Frame(bg = "orange")
        self.container = tk.Frame(bg = "white")
        self.bookCL = searchCollection
        style = ttk.Style(self.container)
        style.configure("Treeview", rowheight = 100 , font=("Helvetica", 16), anchor = tk.CENTER , justify = tk.CENTER)
        style.configure("Treeview.Heading", font=("Helvetica", 16))
        scroll_y = tk.Scrollbar(self.container)

        treeCat = ttk.Treeview(self.container ,yscrollcommand = scroll_y.set)
        treeCat.heading('#0', text = 'Categories')

        self.treeBooks = ttk.Treeview(self.container,column = ("#1 , #2 , #3, #4"), height = 10 , selectmode = "browse")
        self.treeBooks.column('#0', width = 300 , minwidth = 300, stretch = tk.NO)
        self.treeBooks.column('#1', width=180, minwidth = 180, stretch=tk.NO)
        self.treeBooks.column('#2', width=180, minwidth=180, stretch=tk.NO)
        self.treeBooks.column('#3', width=180, minwidth=180, stretch=tk.NO)
        self.treeBooks.column('#4', width=140, minwidth=140, stretch=tk.NO)

        self.treeBooks.heading('#0', text = "Book", anchor = 'center')
        self.treeBooks.heading('#1' , text = "Author", anchor = 'center')
        self.treeBooks.heading('#2', text="Ganre", anchor='center')
        self.treeBooks.heading('#3', text="Pages", anchor='center')
        self.treeBooks.heading('#4', text="Rank", anchor='center')
        self.treeBooks.bind("<Double-1>", self.OnDoubleClick)

        login_btn = tk.Button(self.toolbar, text='Login', bg='white', command=self.init_Login, bd=1, compound=tk.TOP,
                              width=15 , font=("Helvetica", 16))
        user_btn = tk.Button(self.toolbar, text='User info', bg='white', command=self.init_User, bd=1, compound=tk.TOP,
                              width=15 , font=("Helvetica", 16))
        basket_btn = tk.Button(self.toolbar, text='Basket', bg='white', command=self.init_Basket, bd=1, compound=tk.TOP,
                              width=15 , font=("Helvetica", 16))
        search_btn = tk.Button(self.toolbar, text='Search', bg='white', command=self.init_Search, bd=1, compound=tk.TOP,
                               width=15 , font=("Helvetica", 16))
        self.search = ttk.Entry(self.toolbar)
        self.search.place(x = 300 , y = 1 , height = 38, width = 869)

        global booksCollection , authenticated
        for x in self.bookCL:
            _img = ImageTk.PhotoImage(x.image , height= 100 , width= 100)
            self.treeBooks.insert('','end', text = x.name  , image = _img,  values = ( x.author.name , x.ganre , x.pages , x.author.rank) )
            self.label = tk.Label(self.container, image=_img)
            self.label.image = _img

        if authenticated:
            user_btn.place(x=1, y=1, height=38, width=100)
        else:
            login_btn.place(x=1, y=1, height=38, width=100)
        scroll_y.pack(side=tk.RIGHT, fill='y')
        scroll_y.config(command = self.treeBooks.yview)
        basket_btn.place(x=199, y=1, height=38, width=100)
        search_btn.place(x=1174, y=1, height=38, width=105)
        treeCat.place(x = 0 , y = 0 , height = 680 , width = 300)
        self.treeBooks.place(x = 300 , y = 0 , width = 980 , height = 680)

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
        global buttonframe , container
        buttonframe, container = userPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)

    def init_Search(self):
        global buttonframe, container , searchCollection , booksCollection

        if self.search.get() != '':
            searchCollection = []
            for x in booksCollection:
                if self.search.get() in x.name:
                    searchCollection.append(x)
        else:
            searchCollection = booksCollection

        mainPage = MainPage(self)
        buttonframe, container = mainPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)

    def OnDoubleClick(self, event):
        global booksCollection , mainBook , buttonframe , container
        for book in booksCollection:
            if book.name == self.treeBooks.item(self.treeBooks.selection(),"text"):
                mainBook = book
                break
        print(mainBook.purchased)
        bookPage = BookPage(self)
        buttonframe, container = bookPage.show()
        buttonframe.place(x=0, y=0, width=1280, height=40)
        container.place(x=0, y=40, width=1280, height=680)
