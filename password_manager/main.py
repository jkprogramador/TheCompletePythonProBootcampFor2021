from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    new_password = PasswordGenerator.generate()
    password_input.delete(0, END)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_input.get().strip()

    if 0 == len(website):
        messagebox.showerror(title="Oops!", message="Please do not leave the website field empty.")
    else:
        try:
            with open("data.json") as file:
                data = json.load(file)

                if website in data:
                    messagebox.showinfo(title=website,
                                        message=f"Website: {website} \
                                        \n Email: {data[website]['email']} \
                                         \nPassword: {data[website]['password']}")
                else:
                    messagebox.showinfo(title=website, message="No details for the website exist.")
        except FileNotFoundError:
            messagebox.showinfo(title="Oops!", message="No Data File Found.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def is_data_valid(website: str, password: str) -> bool:
    return 0 != len(website) and 0 != len(password)


def write_file(**kwargs: dict):
    new_data = {
        kwargs["website"]: {
            "email": kwargs["email"],
            "password": kwargs["password"]
        }
    }

    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)


def clear_fields():
    website_input.delete(0, END)
    password_input.delete(0, END)


def save_records():
    website = website_input.get().strip()
    email = email_input.get().strip()
    password = password_input.get().strip()

    if not is_data_valid(website=website, password=password):
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        write_file(website=website, email=email, password=password)
        clear_fields()
        website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0, sticky="E")

website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, sticky="W", padx=20, pady=5)

search_btn = Button(text="Search", width=10, command=find_password)
search_btn.grid(row=1, column=2, sticky="W", pady=5)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, sticky="E")

email_input = Entry(width=35)
email_input.insert(END, "jkprogramador@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, sticky="W", padx=20, pady=5)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky="E")

password_input = Entry(width=35)
password_input.grid(row=3, column=1, sticky="W", padx=20, pady=5)

password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=3, column=2, sticky="W", pady=5)

add_btn = Button(text="Add", width=30, command=save_records)
add_btn.grid(row=4, column=1, sticky="W", padx=20, pady=10)
window.mainloop()
