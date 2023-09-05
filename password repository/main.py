from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import pandas as pd
from random import randint, choice, shuffle
import pyperclip
import json

with open('password.txt') as data:
        txt = data.read()
print(txt)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list = password_list + [choice(symbols) for char in range(randint(2, 4))]
    password_list = password_list + [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0, password)
    
    pyperclip.copy(password)
        
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = email_entry.get()
    password = password_entry.get()
    # Turn input value to dictionary
    new_data = {
        website:{
            'email':user,
            'password':password
        }
    }
    # 
    
    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showinfo(title = 'OOPS', message = "Please don't leave any fields empty!")
    else:   
        is_ok = messagebox.askokcancel(title = website, message = f"These are the details entered: \nEmail: {website}\npassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open('password.json', 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # file.writelines(f"{website} | {user} | {password}\n")
            except FileNotFoundError:
                with open('password.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent = 4)
                
            else:      
                # Updating old data with new data
                data[website] = new_data[website]
            # Saving updated data
                with open('password.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            # insert new records to txt file
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        
    
    # with open('password.txt') as data:
    #     txt = data.read()

# ---------------------------- SEARCH PASSWORD ------------------------ #   

def search():
    try:
        website = website_entry.get()
        with open('password.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = 'Error', message = 'No data file found') 
    else:  
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title = website, message = f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title = 'Error', message = f"No data for {website} exists")




import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# # ADDED
# def copy_account_to_clipboard():
#     text_to_copy = website_entry.get()
#     if text_to_copy:
#         window.clipboard_clear()  # Clear the clipboard
#         window.clipboard_append(text_to_copy)  # Copy the text to the clipboard
#         window.update()  # Update the clipboard
#         show_copy_popup()
#     else:
#         messagebox.showwarning("Clipboard Copy", "No text to copy.")

# def show_copy_popup():
#     popup = tk.Toplevel(window)
#     popup.title("Clipboard Copy")
    
#     label = ttk.Label(popup, text="Text copied to clipboard.")
#     label.pack(padx=20, pady=10)
    
#     ok_button = ttk.Button(popup, text="OK", command=popup.destroy)
#     ok_button.pack(pady=10)
    
#     # Position the popup in the center of the screen
#     popup.geometry("+{}+{}".format(root.winfo_screenwidth() // 2 - popup.winfo_reqwidth() // 2,
#                                    root.winfo_screenheight() // 2 - popup.winfo_reqheight() // 2))
#     popup.transient(root)  # Make the popup window transient (closes when main window closes)
#     popup.grab_set()  # Grab focus on the popup
#     root.wait_window(popup)  # Wait for the popup window to be closed

            
# ---------------------------- UI SETUP ------------------------------- #


# # window
# window = Tk()
# window.title('Password Manager')
# window.config(padx = 25, pady = 25, bg = 'white')

# # canvas
# canvas = Canvas(width = 250,height = 250)
# img = PhotoImage(file = 'logo.png')
# canvas.create_image(100, 100, image = img)
# canvas.config(bg = 'white')
# canvas.grid(column = 1, row = 0)

# # label
# label_web = Label(window, text = 'Website: ', bg = 'white', fg = 'black')
# label_web.grid(column = 0, row = 1, pady=3)

# label_eu = Label(window,text = 'Email/Username: ', bg = 'white', fg = 'black')
# label_eu.grid(column = 0, row = 2, pady=3)

# label_pa = Label(window,text = 'Password: ', bg = 'white', fg = 'black')
# label_pa.grid(column = 0, row = 3, pady=3)

# # entry
# entry_web = Entry(window, width = 35, bg = 'white', fg = 'black')
# entry_web.grid(column = 1, row = 1, columnspan = 2, pady=3)

# entry_eu = Entry(window, width = 35,bg = 'white', fg = 'black')
# entry_eu.grid(column = 1, row = 2, columnspan = 2, pady=3)

# entry_pa = Entry(window, width = 24, bg = 'white', fg = 'black')
# entry_pa.grid(column = 1, row = 3, pady=3)

# # button
# button_add = Button(window, bg = 'white', width = 33, text = 'Add', borderwidth=-1,highlightbackground="white", highlightthickness=1)
# button_add.grid(column = 1, row = 4, columnspan = 2, pady=3)
# Button()
# button_gen = Button(window, bg = 'white', text = 'Generate', relief = "solid", bd = 0)
# button_gen.grid(column = 2, row = 3, columnspan = 2, pady=3)

# window.mainloop()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "peacefrank751215@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password",width=11, font={'arial', 9}, command = pass_gen)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, font={'arial', 9}, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", font={'arial', 9}, command=search)
search_button.grid(row=1, column=2)

# copy email button
# copy_account_button = Button(text="Copy password to Clipboard", command=copy_to_clipboard)


# copy password button
# copy_pass_button = Button(text="Copy pawword to Clipboard", command=copy_to_clipboard)



window.mainloop()