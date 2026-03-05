import tkinter as Tk
from tkinter import messagebox
from user_class import User
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import encrypt
import decrypt
import hashlib

# Creating supabase client from hidden env file
load_dotenv() 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

# Main program
def main_program():
    pass

# Save sign up details to database
def signup_submit(username, password):
    global supabase
    username = encrypt.encrypt(username)
    password = encrypt.encrypt(password)
    password = hashlib.sha256(password.encode()).hexdigest()
    response = supabase.table("users").insert({"username": username, "password": password}).execute()

# Checking for unique username when users sign up
def check_username(username,password):
    username_encrypted = encrypt.encrypt(username)
    response = supabase.table("users").select("username").eq("username", username_encrypted).execute()

    if len(response.data) > 0:
        messagebox.showerror(title="Error", message="That username is already taken!")
    else:
        signup_submit(username, password)

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

    submit_btn = Tk.Button(signup, text="Sign up", command=lambda: (check_username(signup_username.get(), signup_password.get()))).pack()
    signup_btn = Tk.Button(signup, text="Log in instead", command=lambda: (signup.destroy(), login())).pack()

def check_login(username, password):
    username_encrypted = encrypt.encrypt(username)
    password_encryped = encrypt.encrypt(password)
    password_hashed = hashlib.sha256(password_encryped.encode()).hexdigest()
    response = supabase.table("users").select("*").eq("username", username_encrypted).eq("password", password_hashed).execute()

    if len(response.data) > 0:
        main_program()
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

    submit_btn = Tk.Button(login, text="Log in", command=lambda: (check_login(login_username.get(), login_password.get()))).pack()
    signup_btn = Tk.Button(login, text="Sign up instead", command=lambda: signup(login)).pack()

    login.mainloop()

# Running login when the app opens
if __name__ == "__main__":
    login()
