from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Question(text=data["question"], answer=data["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.has_questions():
    quiz.next_question()
    quiz.print_score()

print("You've completed the quiz.")
final_score = quiz.get_score()
question_number = quiz.get_question_number()
print(f"Your final score was: {final_score}/{question_number}")
