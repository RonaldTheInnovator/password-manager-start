from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    # password_letters = [new_item for item in range] LIST COMPREHENSION

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_symbol + password_numbers

    random.shuffle(password_list)


    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()




    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        its_not_ok = messagebox.showinfo(title="Oops", message="Please dont leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {username} "
                                                     f"\nPassword: {password} \nIs it ok to save")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0,END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200,height=200)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=mypass_image)
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add",width=36,command=save)
website_entry = Entry(width=35)
username_entry = Entry(width=35)
password_entry = Entry(width=21)






canvas.grid(column=1,row=0)

website_label.grid(column=0,row=1)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

username_label.grid(column=0,row=2)
username_entry.grid(column=1,row=2,columnspan=2)
username_entry.insert(0,"someone@email.com")

password_label.grid(column=0,row=3)
password_entry.grid(column=1,row=3)

generate_button.grid(column=2,row=3)

add_button.grid(column=1,row=4,columnspan=2)















window.mainloop()