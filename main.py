from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=500,height=500)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(250,250,image=mypass_image)
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
generate_button = Button(text="Generate Password:")
add_button = Button(text="Add",width=36)
website_entry = Entry(width=35)
username_entry = Entry(width=35)
password_entry = Entry(width=21)






canvas.grid(column=1,row=0)
website_label.grid(column=0,row=1)
website_entry.grid(column=1,row=1,columnspan=2)
username_label.grid(column=0,row=2)
username_entry.grid(column=1,row=2,columnspan=2)
password_label.grid(column=0,row=3)
password_entry.grid(column=1,row=3)
generate_button.grid(column=2,row=3)
add_button.grid(column=1,row=4,columnspan=2)















window.mainloop()