from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from services import RegistrationPage,my_dashboard

# Functionality
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)

def login():
    # Dummy login function for demonstration
    username = usernameEntry.get()
    password = passwordEntry.get()
    print("Login Attempt:")
    print("Username:", username)
    print("Password:", password)
    messagebox.showinfo("Login", "Login Successful!")
    open_dashboard()
    # Perform actual login validation here
    if username == "admin" and password == "admin":
        print("Login successful")
        open_dashboard()
    else:
        print("Login failed")

def open_dashboard():
    my_dashboard()
    
def hide():
    open_eye.config(file=os.path.join('images', 'closeeye.png'))
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    open_eye.config(file=os.path.join('images', 'openeye.png'))
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def open_registration_page():
    registration_window = Toplevel(login_window)
    registration_window.geometry('500x300')
    registration_window.title('Registration Page')
    RegistrationPage(registration_window)

# GUI
login_window = Tk()
login_window.geometry('920x668+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')

# Load background image
bg_path = os.path.join('images', 'background.jpg')
bg_image = Image.open(bg_path)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(login_window, image=bg_photo)
bg_label.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.insert(0, 'Username')
usernameEntry.place(x=580, y=200)
usernameEntry.bind('<FocusIn>', user_enter)
Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.insert(0, 'Password')
passwordEntry.place(x=580, y=260)
passwordEntry.bind('<FocusIn>', password_enter)
Frame(login_window, width=250, height=2, bg='firebrick1').place(x=580, y=282)

open_eye = PhotoImage(file=os.path.join('images', 'openeye.png'))
eyeButton = Button(login_window, image=open_eye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white',
                      cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1')
forgetButton.place(x=715, y=295)

login_button = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                      activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19,
                      command=open_dashboard) 
login_button.place(x=578, y=350)


orLabel = Label(login_window, text='---------------OR--------------', font=('Open Sans', 16), fg='firebrick1', bg='white')
orLabel.place(x=583, y=400)

facebook_logo = PhotoImage(file=os.path.join('images', 'facebook.png'))
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=648, y=440)

google_logo = PhotoImage(file=os.path.join('images', 'google.png'))
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file=os.path.join('images', 'twitter.png'))
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=730, y=440)

signupLabel = Label(login_window, text='Donot have an account?', font=('Open Sans', 9, 'bold'), fg='firebrick1',
                    bg='white', cursor='hand2')
signupLabel.place(x=590, y=500)

new_account_button = Button(login_window, text='Create new one', font=('Open Sans', 9, 'bold underline'), fg='blue',
                            bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                            command=open_registration_page)
new_account_button.place(x=740, y=500)

login_window.mainloop()
