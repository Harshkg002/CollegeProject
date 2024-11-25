from tkinter import *
from tkinter import messagebox as ms
import smtplib
from email.message import EmailMessage
import random
import mysql.connector as mc
from PIL import Image,ImageTk
from devtools import *

class Signup:

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

    def send_otp(self):
        email = self.email_entry.get()
        self.otp = str(random.randint(100000, 999999))
        msg = EmailMessage()
        msg.set_content(f"Your OTP is: {self.otp}")
        msg["Subject"] = "Email Verification OTP"
        msg["From"] = "akshsaini1908@gmail.com"
        msg["To"] = email

        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("akshsaini1908@gmail.com", "xtkw wxwe yuac ispv")  # Replace with actual password
            server.send_message(msg)
            server.quit()
            self.result_label.config(text="OTP sent successfully", fg="green")
        except Exception as e:
            ms.showerror("ERROR", f"Failed to send OTP: {e}")

    def verify_otp(self):
        otp = self.otp_entry.get()
        if otp == self.otp:
            self.result_label.config(text="Email is verified", fg="green")
        else:
            self.result_label.config(text="Invalid OTP", fg="red")

    def database(self, event):
        if self.name.get()=="" or self.email_entry.get()=="" or self.passw.get()=="" : 
            ms.showerror("ERROR","Please try again")

        elif len(self.passw.get())<6:
            ms.showerror('Error','Password is weak')
            self.passw.delete(0,END)

        else :
            con=mc.connect(host="localhost",user="root",password="aniket@12",database="backend") 
            cur=con.cursor() 
            cur.execute("insert into userdata (username,email,passwordd)values(%s,%s,%s)",(self.name.get(),self.email_entry.get(),self.passw.get()))
            con.commit()
            ms.showinfo("SUCCESS","Sign up succesfully")
            self.root.destroy()
            import loginpg as l
            obj=l.login()

    #def back(self):
         #import loginpg as p
         #self.root.destroy()
         #object=p.login()


    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        window_width=925
        window_height=500
        center_window(self.root,window_width,window_height)

        self.img = PhotoImage(file=find_file("login.png"))
        Label(self.root, image=self.img, bg="white").place(x=50, y=50)

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=30)

        self.heading = Label(self.frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, 'bold'))
        self.heading.place(x=100, y=5)

        self.name = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.name.place(x=30, y=60)
        self.name.insert(0, "Username")  # Placeholder text
        self.name.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.name, "Username"))
        self.name.bind("<FocusOut>", lambda event: self.on_focusout(event, self.name, "Username"))
        self.name.config(highlightthickness=0)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=87)

        self.email_entry = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.email_entry.place(x=30, y=180)
        self.email_entry.insert(0, "Email")  # Placeholder text
        self.email_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.email_entry, "Email"))
        self.email_entry.bind("<FocusOut>", lambda event: self.on_focusout(event, self.email_entry, "Email"))
        self.email_entry.config(highlightthickness=0)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=147)

        self.passw = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.passw.place(x=30, y=120)
        self.passw.insert(0, "Password")  # Placeholder text
        self.passw.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.passw, "Password"))
        self.passw.bind("<FocusOut>", lambda event: self.on_focusout(event, self.passw, "Password"))
        self.passw.config(highlightthickness=0)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=267)

        self.otp_entry = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.otp_entry.place(x=30, y=240)
        self.otp_entry.insert(0, "OTP")  # Placeholder text
        self.otp_entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.otp_entry, "OTP"))
        self.otp_entry.bind("<FocusOut>", lambda event: self.on_focusout(event, self.otp_entry, "OTP"))
        self.otp_entry.config(highlightthickness=0)

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=207)

        self.result_label = Label(self.frame, text="", fg="green", bg="white", font=("Microsoft YaHei UI Light", 11))
        self.result_label.place(x=30, y=270)

        # Create button to send OTP
        self.send_button = Button(self.root, text="Send OTP", bd=0, command=self.send_otp)
        self.send_button.place(x=730, y=210, width=80)
        self.send_button.config(highlightthickness=0)

        # Create button to verify OTP
        self.verify_button = Button(self.root, text="Verify", bd=0, command=self.verify_otp)
        self.verify_button.place(x=730, y=270)
        self.verify_button.config(highlightthickness=0)

        # Initialize OTP
        self.otp = ""

        # Create Sign Up button
        self.but1 = Button(self.frame, text="Sign up", bg="white", fg="#57a1f8", border=0)
        self.but1.place(x=35, y=310, width=300, height=40)
        self.but1.bind("<Button-1>", self.database)

        self.__path1 = find_file("backbut.pmg")
        self.__original1 = Image.open(self.__path1)
        self.__resized1 = self.__original1.resize((30, 30))
        self.__fimage1 = ImageTk.PhotoImage(self.__resized1)
        self.__label1 = Label(self.root, image=self.__fimage1)
        self.__label1.place(x=10, y=10)
        self.__label1.bind('<Button-1>',self.back())
        self.__label1.config(bd=0,highlightthickness=0)

