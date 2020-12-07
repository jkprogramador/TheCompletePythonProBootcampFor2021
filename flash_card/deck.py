import pandas
import random
from card import Card


class Deck:
    def __init__(self):
        self.__cards = self.__load()
        self.__current_card = None

    @staticmethod
    def __load() -> list:
        """Load deck of Card objects."""
        try:
            df = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            df = pandas.read_csv("data/french_words.csv")
        finally:
            data = df.to_dict(orient="records")

        return [Card(item) for item in data]

    def get_cards(self) -> list:
        return self.__cards

    def get_current_card(self) -> Card:
        return self.__current_card

    def get_random_card(self) -> Card:
        self.__current_card = random.choice(self.__cards)
        return self.__current_card

    def remove_current_card(self):
        self.__cards.remove(self.__current_card)
        self.__current_card = None

    def save(self):
        df = pandas.DataFrame([card.to_dict() for card in self.__cards])
        df.to_csv("data/words_to_learn.csv", index=False)
