import discount
import basket

class User:
    __doc__ = "User class"

    def __init__(self, login: str, password: str, userDiscount: discount, basket: basket) -> None:
        self.login = login
        self.password = password
        self.deposit = 1000
        self.userDiscount = userDiscount
        self.basket = basket
        self.purchaseList = []
