import datetime

class Author:
    __doc__ = "Author class"

    def __init__(self, name: str, surname: str, rank: int, birthdate: datetime.date) -> None:
        self.name = name
        self.surname = surname
        self.rank = rank
        self.birthdate = birthdate

