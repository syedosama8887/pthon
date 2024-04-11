from tkinter import *
class RegistrationPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Registration Page")
        self.master.configure(bg='white')
        
        # Heading
        self.heading = Label(master, text="Registration Page", font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
        self.heading.grid(row=0, columnspan=2, padx=10, pady=20)

        # Username
        self.label_username = Label(master, text="Username:", font=('Microsoft Yahei UI Light', 12), bg='white', fg='firebrick1')
        self.label_username.grid(row=1, column=0, padx=10, pady=5, sticky=E)
        self.entry_username = Entry(master, bg='white', fg='firebrick1', bd=2)
        self.entry_username.grid(row=1, column=1, padx=10, pady=5, sticky=W+E)

        # Password
        self.label_password = Label(master, text="Password:", font=('Microsoft Yahei UI Light', 12), bg='white', fg='firebrick1')
        self.label_password.grid(row=2, column=0, padx=10, pady=5, sticky=E)
        self.entry_password = Entry(master, show="*", bg='white', fg='firebrick1', bd=2)
        self.entry_password.grid(row=2, column=1, padx=10, pady=5, sticky=W+E)

        # Email
        self.label_email = Label(master, text="Email:", font=('Microsoft Yahei UI Light', 12), bg='white', fg='firebrick1')
        self.label_email.grid(row=3, column=0, padx=10, pady=5, sticky=E)
        self.entry_email = Entry(master, bg='white', fg='firebrick1', bd=2)
        self.entry_email.grid(row=3, column=1, padx=10, pady=5, sticky=W+E)

        # Register Button
        self.register_button = Button(master, text="Register", bg='firebrick1', fg='white', command=self.register)
        self.register_button.grid(row=4, columnspan=2, padx=10, pady=20)

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()

        # Here you can add your registration logic, like storing the user details in a database, etc.
        print("Username:", username)
        print("Password:", password)
        print("Email:", email)# Create the main application window
# root = Tk()
# registration_page = RegistrationPage(root)
# root.mainloop()
