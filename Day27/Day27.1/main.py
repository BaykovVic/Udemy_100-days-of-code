import tkinter
import turtle

window = tkinter.Tk()

window.title("My First GUI Window")
window.minsize(width=500, height=300)


#Label
label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
label.pack()
tim = turtle.Turtle()
tim.write("Some text", font=("Times New Roman", 80, "bold"))
window.mainloop()