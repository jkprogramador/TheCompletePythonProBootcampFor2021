import tkinter

window = tkinter.Tk()
window.title("My First Tkinter program")
window.minsize(width=500, height=300)

# Label.
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack()


# Button.
def btn_click():
    my_label.config(text=my_input.get())


button = tkinter.Button(text="Click me", command=btn_click)
button.pack()

# Entry.
my_input = tkinter.Entry(width=50)
my_input.insert(tkinter.END, string="Some text to begin with.")
my_input.pack()

# Text.
my_text = tkinter.Text(height=5, width=30)
my_text.focus()
my_text.pack()
my_text.insert(tkinter.END, "Example of multi-line text entry.")


# Spinbox.
def spinbox_used():
    print(my_spinbox.get())


my_spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
my_spinbox.pack()


# Scale.
def scale_used(value):
    print(value)


my_scale = tkinter.Scale(from_=0, to=100, command=scale_used)
my_scale.pack()


# Checkbutton.
def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
my_checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
my_checkbutton.pack()


# Radiobutton.
def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radio_button_1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button_2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()


# Listbox.
def listbox_used(event):
    print(my_listbox.get(my_listbox.curselection()))


my_listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Orange", "Banana"]
for item in fruits:
    my_listbox.insert(fruits.index(item), item)

my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()
window.mainloop()
