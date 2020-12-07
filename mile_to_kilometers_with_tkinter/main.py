import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

my_input = tkinter.Entry(width=20, justify="center")
my_input.insert(tkinter.END, string="0")
my_input.focus()
my_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)


def convert():
    miles = float(my_input.get())
    km = round(miles * 1.609344, 5)
    result_label.config(text=f"{km}")


button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)
window.mainloop()
