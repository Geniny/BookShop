import discount
import basket
from PIL import Image

class User:
    __doc__ = "User class"

    def __init__(self, login: str, password: str, userDiscount: discount, basket: basket , email: str , initials: str , imagepath: str) -> None:
        self.image = Image.open(imagepath)
        self.initials = initials
        self.birthdate = 2000
        self.city = "Minsk"
        self.avatar = "avatar"
        self.login = login
        self.password = password
        self.deposit = 1000
        self.userDiscount = userDiscount
        self.email = email
        self.basket = basket
        self.purchaseList = []
        self.count = self.getCount()

    def getCount(self):
        i = 0
        if self.purchaseList != []:
            for x in self.purchaseList:
                i += 1
            return i
        else:
            return 0
