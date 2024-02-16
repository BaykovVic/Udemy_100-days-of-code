from tkinter import *

#Window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
label = Label(text="I'm a label", font=("Arial", 24, "bold"))
label.pack()

label["text"] = "New Text"
label.config(text="Another text")

def on_button_click():
    #label.config(text="Button Got Clicked")
    label.config(text=input.get())

#Button
button = Button(text="Click me", command=on_button_click)
button.pack()

#Entry
input = Entry(width=10)
input.pack()
#print(input.get())

window.mainloop()