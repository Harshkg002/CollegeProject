from tkinter import *
from tkinter import messagebox as ms 
import mysql.connector as mc
from devtools import *


class login:

    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        window_width=925
        window_height=500
        center_window(self.root,window_width,window_height)

        self.img = PhotoImage(file=find_file("login.png"))
        Label(self.root, image=self.img, bg="white").place(x=50, y=50)

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        self.heading = Label(self.frame, text="Login", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Create Entry for Username
        self.user = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "Email")  # Placeholder text
        self.user.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.user, "Email"))  # Clear on click
        self.user.bind("<FocusOut>", lambda event: self.on_focusout(event, self.user, "Email"))  # Restore if empty

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Create Entry for Password
        self.passw = Entry(self.frame, width=25, fg="grey", bd=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.passw.place(x=30, y=150)
        self.passw.insert(0, "Password")  # Placeholder text
        self.passw.bind("<FocusIn>", lambda event: self.on_entry_click(event, self.passw, "Password"))  # Clear on click
        self.passw.bind("<FocusOut>", lambda event: self.on_focusout(event, self.passw, "Password"))  # Restore if empty

        Frame(self.frame, width=295, height=2, bg="black").place(x=25, y=177)

        self.user.config(highlightthickness=0)
        self.passw.config(highlightthickness=0)

        # Buttons and Labels
        self.but1 = Button(self.frame, text="Login", bg="white", fg="#57a1f8", border=0)
        self.but1.place(x=35, y=220, width=300, height=40)
        self.but1.bind("<Button-1>",self.fetchdb)

        self.lbl1 = Label(self.root, text="Don't have an account? Create one", fg="black", bg="white", font=(12))
        self.lbl1.place(x=520, y=340)

        self.butt=Button(self.root, text='Sign up', fg='#57a1f8', bd=0, font=('Arial Bold',12))
        self.butt.place(x=740, y=345, height=15, width=60)
        self.butt.bind("<Button-1>",self.next)
        self.butt.config(highlightthickness=0)

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

    def next(self,event=None):
        import signuppg as s
        self.root.destroy()
        new_root=Tk()
        obj=s.Signup(new_root)

    def fetchdb(self, event):
        """Method to handle the login process."""
    
    # Check if the fields are empty
        if self.user.get() == "" or self.passw.get() == "":
            ms.showerror("ERROR", "Please fill in both fields")
            return

        try:
            # Connect to the MySQL database
            con = mc.connect(host='localhost', user='root', password='password', database='database')
            cur = con.cursor()

            # Parameterized query to prevent SQL injection
            query = 'SELECT * FROM userdata WHERE email = %s AND passwordd = %s'
            cur.execute(query, (self.user.get(), self.passw.get()))

            # Fetch one record
            user_record = cur.fetchone()

            # Check if a record was found
            if user_record:
                ms.showinfo("Success", "Login successful!")  # You can redirect to another window here
                # You can implement further logic here for a successful login
            else:
             ms.showerror("ERROR", "Invalid email or password. Please try again.")

        except mc.Error as e:
            ms.showerror("Database Error", f"An error occurred: {e}")
    
        finally:
            # Close the cursor and connection
            cur.close()
            con.close()
                    
            

# Create an instance of the Signup class
#object = login()
