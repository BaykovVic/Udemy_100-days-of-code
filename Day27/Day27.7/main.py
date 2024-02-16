from tkinter import *

def calculate() -> float:
    return float(input.get()) * 1.609

def set_result():
    result_label["text"] = calculate()

#Window
window = Tk()
window.title("My First GUI Program")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_to_label = Label(text="Is equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

result_label = Label(text="0")
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

result_units_label = Label(text="km")
result_units_label.grid(column=2, row=1)
result_units_label.config(padx=10, pady=10)

button_calculate = Button(text="Calculate", command=set_result)
button_calculate.grid(column=1, row=2)
button_calculate.config(padx=10, pady=10)

window.mainloop()

