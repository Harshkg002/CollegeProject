from tkinter import *
from tkinter import messagebox as ms 
from centerwindow import *
import smtplib
from email.message import EmailMessage
import random
import mysql.connector  # Make sure to install this package if not already installed

class reset:

    def send_otp(self):
        email = self.user.get()
        self.otp = str(random.randint(100000, 999999))
        msg = EmailMessage()
        msg.set_content(f"Dear Customer \n\n\nThank you for registering with Degree Bee!\n\nYour One Time Code: {self.otp}\n\n\nIf you didn’t request this code, please ignore this email.\n\nFor any questions or support, feel free to contact our team at degreebeeofficial@gmail.com.\n\nBest regards\nThe Degree Bee Team ")
        msg["Subject"] = "Email Verification OTP"
        msg["From"] = "degreebeeofficial@gmail.com"
        msg["To"] = email

        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("degreebeeofficial@gmail.com", "lsjx ltlr qfiu fkyi")  # Replace with actual password
            server.send_message(msg)
            server.quit()
            self.result_label.config(text="OTP sent successfully", fg="green")
        except Exception as e:
            ms.showerror("ERROR", f"Failed to send OTP: {e}")

    def verify_otp(self):
        otp = self.otp_entry.get()
        if otp == self.otp:
            self.result_label.config(text="Email is verified", fg="green")
            self.show_password_entry()
        else:
            self.result_label.config(text="Invalid OTP", fg="red")

    def show_password_entry(self):
        # Show the new password entry field and update button
        self.new_password_label = Label(self.frame, text="Enter New Password", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.new_password_label.place(x=30, y=200)

        self.new_password_entry = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.new_password_entry.place(x=30, y=230)
        self.new_password_entry.insert(0, "New Password")  # Placeholder text
        self.new_password_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.new_password_entry, "New Password"))
        self.new_password_entry.bind("<FocusOut>", lambda event: self.on_focusout(event, self.new_password_entry, "New Password"))
        self.new_password_entry.config(highlightthickness=0)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=252)

        self.update_password_button = Button(self.frame, text="Update Password", bg="white", fg="#57a1f8", border=0, command=self.update_password)
        self.update_password_button.place(x=35, y=280, width=300, height=40)

    def update_password(self):
        new_password = self.new_password_entry.get()
        email = self.user.get()

        if new_password and new_password != "New Password":
            # Update the password in the SQL database
            try:
                
                connection = mysql.connector.connect(
        host='localhost',  # or your server IP
        user='root',
        password='7015555218',
        database='backend'
                )
             
                cursor = connection.cursor()
                update_query = "UPDATE userdata SET passwordd = %s WHERE email = %s"
                cursor.execute(update_query, (new_password, email))
                connection.commit()
                cursor.close()
                connection.close()
                ms.showinfo("Success", "Password updated successfully!")
                import loginpg as l
                self.root.quit()  # Close the application or redirect as needed
                obj=l.login()
            except mysql.connector.Error as err:
                ms.showerror("ERROR", f"Failed to update password: {err}")
        else:
            ms.showwarning("Warning", "Please enter a valid password.")

    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        window_width=925
        window_height=500
        center_window(self.root, window_width, window_height)

        self.img = PhotoImage(file="/Users/akshsaini/Documents/PYproject//login.png")
        Label(self.root, image=self.img, bg="white").place(x=50, y=50)

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        self.heading = Label(self.frame, text="Forgot password", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Create Entry for Username
        self.user = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=85)
        self.user.insert(0, "Email")  # Placeholder text
        self.user.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.user, "Email"))  # Clear on click
        self.user.bind("<FocusOut>", lambda event: self.on_focusout(event, self.user, "Email"))  # Restore if empty
        self.user.config(highlightthickness=0)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Create Entry for OTP
        self.otp_entry = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.otp_entry.place(x=30, y=155)
        self.otp_entry.insert(0, "OTP")  # Placeholder text
        self.otp_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.otp_entry, "OTP"))
        self.otp_entry.bind("<FocusOut>", lambda event: self.on_focusout(event, self.otp_entry, "OTP"))
        self.otp_entry.config(highlightthickness=0)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=177)

        # Create button to send OTP
        self.send_button = Button(self.root, text="Send OTP", bd=0, command=self.send_otp)
        self.send_button.place(x=730, y=150, width=80)
        self.send_button.config(highlightthickness=0)

        # Create button to verify OTP
        self.verify_button = Button(self.root, text="Verify", bd=0, command=self.verify_otp)
        self.verify_button.place(x=730, y=220)
        self.verify_button.config(highlightthickness=0)

        # Initialize OTP
        self.otp = ""

        # Buttons and Labels
        '''self.but1 = Button(self.frame, text="Next", bg="white", fg="#57a1f8", border=0)
        self.but1.place(x=35, y=220, width=300, height=40)
        self.but1.bind("<Button-1>")'''

        self.result_label = Label(self.frame, text="", fg="green", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.result_label.place(x=30, y=180)        

        self.root.mainloop()

    def on_entry_click(self, event, entry, placeholder):
        """Function to clear the placeholder text when the entry is clicked."""
        if entry.get() == placeholder:
            entry.delete(0, "end")  # Clear the current text
            entry.config(fg='black')  # Change text color to black

    def on_focusout(self, event, entry, placeholder):
        """Function to restore the placeholder text if the entry is empty."""
        if entry.get() == '':
            entry.insert(0, placeholder)  # Restore placeholder text
            entry.config(fg='grey')  # Change text color to grey

#obj = reset()