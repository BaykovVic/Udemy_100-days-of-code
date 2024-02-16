from tkinter import *

#Window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
label = Label(text="I'm a label", font=("Arial", 24, "bold"))
#label.pack()
#label.place(x=100, y=200)
label.grid(column=0, row=0)

label["text"] = "New Text"
label.config(text="Another text")
label.config(padx=20, pady=20)
def on_button_click():
    #label.config(text="Button Got Clicked")
    label.config(text=input.get())

#Button
button = Button(text="Click me", command=on_button_click)
#button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
#Entry
input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)
#print(input.get())

window.mainloop()