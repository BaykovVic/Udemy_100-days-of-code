import tkinter
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '&', '(', ')', '*', '+', '_']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password= "".join(password_list)
    password_input.insert(0, password)

    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    is_ok = False
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if website == '' or email == '' or password == '':
        messagebox.showerror("Oops!", "Fields cannot be empty!")
    else:
        is_ok = messagebox.showinfo(title=website, message=f"There are details entered:\n "
                                                           f"Email: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)


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


email_label = tkinter.Label(text="Email/Username:", font=("Arial", 14))
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", font=("Arial", 14))
password_label.grid(column=0, row=3)


website_input = tkinter.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = tkinter.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@example.com")
password_input = tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

button_generate = tkinter.Button(text="Generate", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = tkinter.Button(text="Add", width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()