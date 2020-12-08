from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, sticky="E")
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Hello",
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, bd=0, activebackground=THEME_COLOR,
                               command=self.on_true_press)
        self.true_btn.grid(row=2, column=0, sticky="W")
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, bd=0, activebackground=THEME_COLOR,
                                command=self.on_false_press)
        self.false_btn.grid(row=2, column=1, sticky="E")
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=self.quiz.score)
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")

        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def on_true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def on_false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        self.canvas.config(bg="green" if is_right else "red")
        self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
