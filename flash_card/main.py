from tkinter import *
from deck import Deck

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

timer = None


# ------------------------------------- Random word --------------------------------------#


def next_card():
    card = deck.get_random_card()
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word, text=card.front, fill="black")
    global timer
    timer = window.after(3000, flip_card)


def flip_card():
    card = deck.get_current_card()
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word, text=card.back, fill="white")


def on_incorrect():
    window.after_cancel(timer)
    next_card()


def on_correct():
    window.after_cancel(timer)
    deck.remove_current_card()
    deck.save()
    next_card()


# -------------------------------------- UI --------------------------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="title", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="trouve", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=on_incorrect)
wrong_btn.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=on_correct)
right_btn.grid(row=1, column=1)

deck = Deck()
next_card()
window.mainloop()
