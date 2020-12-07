class Question:
    """Class representing a question with a text and an answer."""

    def __init__(self, text: str, answer: str):
        self.__text = text
        self.__answer = answer

    def get_text(self) -> str:
        return self.__text

    def get_answer(self) -> str:
        return self.__answer
