class Card:
    def __init__(self, data: dict):
        self.__front = data["French"]
        self.__back = data["English"]

    @property
    def front(self):
        return self.__front

    @property
    def back(self):
        return self.__back

    def to_dict(self) -> dict:
        """Return the dictionary representation of this class."""
        return {"French": self.__front, "English": self.__back}
