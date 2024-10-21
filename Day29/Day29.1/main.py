import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.pack()
canvas.grid(column=1, row=0)
website_label = tkinter.Label(text="Website:", font=("Arial", 14))
website_label.grid(column=0, row=1)


username_label = tkinter.Label(text="Email/Username:", font=("Arial", 14))
username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", font=("Arial", 14))
password_label.grid(column=0, row=3)


website_input = tkinter.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
username_input = tkinter.Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
password_input = tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

button_generate = tkinter.Button(text="Generate", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = tkinter.Button(text="Add", width=36, command=generate_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()