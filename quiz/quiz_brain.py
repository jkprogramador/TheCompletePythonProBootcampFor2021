from question_model import Question


class QuizBrain:
    """Class representing the logic of the quiz."""

    def __init__(self, questions_list):
        self.__question_number = 0
        self.__questions_list = questions_list
        self.__score = 0

    def get_question_number(self) -> int:
        return self.__question_number

    def get_question(self, number: int) -> Question:
        return self.__questions_list[number]

    def increase_question_number(self):
        self.__question_number += 1

    def get_number_of_questions(self) -> int:
        return len(self.__questions_list)

    def next_question(self):
        number = self.get_question_number()
        question = self.get_question(number)
        text = question.get_text()
        self.increase_question_number()
        user_answer = input(f"Q.{self.get_question_number()}: {text} (True or False): ")
        self.check_answer(user_answer, question.get_answer())

    def has_questions(self) -> bool:
        return self.get_question_number() < self.get_number_of_questions()

    def get_score(self) -> int:
        return self.__score

    def increase_score(self):
        self.__score += 1

    def print_score(self):
        score = self.get_score()
        question_number = self.get_question_number()
        print(f"Your current score is: {score}/{question_number}.")

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.increase_score()
        else:
            print("You got it wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print()
