class Basket:
    __doc__ = "Basket class"

    def __init__(self) -> None:
        self.purchases = []

    def __add__(self, other):
        self.purchases.append(other)