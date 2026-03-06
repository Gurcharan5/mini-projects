import tkinter as Tk
from tkinter import messagebox
from user_class import User
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import encrypt
import hashlib

# Creating supabase client from hidden env file
load_dotenv() 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def make_transaction(balance_variable, current_user, recipient, amount):
    try:
        amount = int(amount)
    except Exception:
        messagebox.showerror(title="Error", message="You did not give a valid amount")

    try:
        if current_user.get_balance() < amount:
            messagebox.showerror(title="Error", message="You do not have enough funds!")
        else:
            encrypt_recipient = encrypt.encrypt(recipient)
            response = supabase.table("users").select("username").eq("username", encrypt_recipient).execute()

            if len(response.data) > 0:
                response = supabase.table("balance").select("balance").eq("username", encrypt_recipient).execute()
                recipient_balance = int(response.data[0]['balance'])
                new_recipient_balance = recipient_balance + amount
                response = supabase.table("balance").update({"balance": new_recipient_balance}).eq("username", encrypt_recipient).execute()
                new_user_balance = current_user.get_balance() - amount
                user_encrypted = encrypt.encrypt(current_user.get_username())
                response = supabase.table("balance").update({"balance": new_recipient_balance}).eq("username", user_encrypted).execute()#
                current_user.set_new_balance(new_user_balance)
                balance_variable.set(current_user.get_balance())
            else:
                messagebox.showerror(title="Invalid details", message="A user with that username was not found")
    except TypeError:
        pass

# Main program
def main_program(username):
    program = Tk.Tk()
    encrypted_username = encrypt.encrypt(username)
    current_balance_var = Tk.IntVar()
    response = supabase.table("balance").select("balance").eq("username", encrypted_username).execute()
    balance = int(response.data[0]['balance'])
    
    current_user = User(username, balance)
    current_balance_var.set(current_user.get_balance())

    balance_label = Tk.Label(program, text="Current balance:").pack()
    balance = Tk.Label(program, textvariable=current_balance_var).pack()

    send_label = Tk.Label(program, text="Send Money").pack()
    send_username_label = Tk.Label(program, text="Recipient username").pack()
    send_username = Tk.Entry(program)
    send_username.pack(padx=15)
    send_amount_label = Tk.Label(program, text="Amount").pack()
    send_amount = Tk.Entry(program)
    send_amount.pack()

    submit_btn = Tk.Button(program, text="Send money", command=lambda: (
        make_transaction(current_balance_var, current_user, send_username.get(), send_amount.get())
    )).pack()

    program.mainloop()

# Save sign up details to database
def signup_submit(username, password):
    global supabase
    temp_username = username
    username = encrypt.encrypt(username)
    password = encrypt.encrypt(password)
    password = hashlib.sha256(password.encode()).hexdigest()
    response = supabase.table("users").insert({"username": username, "password": password}).execute()
    response = supabase.table("balance").insert({"username": username, "balance": 0}).execute()
    main_program(temp_username)

# Checking for unique username when users sign up
def check_username(username,password, window):
    username_encrypted = encrypt.encrypt(username)
    response = supabase.table("users").select("username").eq("username", username_encrypted).execute()

    if len(response.data) > 0:
        messagebox.showerror(title="Error", message="That username is already taken!")
    else:
        signup_submit(username, password)
        window.destroy()

# Signup window for the user to interact with
def signup(window):
    window.destroy()
    signup = Tk.Tk()

    signup_txt = Tk.Label(signup, text="Sign up for a bank account today")
    signup_txt.pack()
    username_label = Tk.Label(signup, text="Enter Username")
    username_label.pack()
    signup_username = Tk.Entry(signup)
    signup_username.pack()
    password_label = Tk.Label(signup, text="Enter Password")
    password_label.pack()
    signup_password = Tk.Entry(signup, show="*")
    signup_password.pack()

    submit_btn = Tk.Button(signup, text="Sign up", command=lambda: (check_username(signup_username.get(), signup_password.get(), signup))).pack()
    signup_btn = Tk.Button(signup, text="Log in instead", command=lambda: (signup.destroy(), login())).pack()

# Function to check login using the database
def check_login(username, password, window):
    username_encrypted = encrypt.encrypt(username)
    password_encryped = encrypt.encrypt(password)
    password_hashed = hashlib.sha256(password_encryped.encode()).hexdigest()
    response = supabase.table("users").select("*").eq("username", username_encrypted).eq("password", password_hashed).execute()

    if len(response.data) > 0:
        window.destroy()
        main_program(username)
    else:
        messagebox.showerror(title="Error", message="Those details are invalid!")

# Login window for the user to interact with
def login():
    login = Tk.Tk()

    login_txt = Tk.Label(login, text="Login to your bank account").pack()
    username_label = Tk.Label(login, text="Enter Username")
    username_label.pack()
    login_username = Tk.Entry(login)
    login_username.pack()
    password_label = Tk.Label(login, text="Enter Password")
    password_label.pack()
    login_password = Tk.Entry(login, show="*")
    login_password.pack()

    submit_btn = Tk.Button(login, text="Log in", command=lambda: (check_login(login_username.get(), login_password.get(), login))).pack()
    signup_btn = Tk.Button(login, text="Sign up instead", command=lambda: signup(login)).pack()

    login.mainloop()

# Running login when the app opens
if __name__ == "__main__":
    login()
