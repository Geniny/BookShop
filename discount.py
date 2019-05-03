class Discount:
    __doc__ = "Discount class"

    def __init__(self, discountType: str) -> None:
        if discountType == "VIP":
            self.userDiscount = 30
        elif discountType == "DEF":
            self.userDiscount = 10
        elif discountType == "NONE":
            self.userDiscount = 0