from tkinter import *
from PIL import Image, ImageTk
from centerwindow import *  # Ensure this module is in the same directory or correctly referenced

class Personalise:
    
    
    def button(self, event=None):
        import personalise2 as h
        import tkinter as tk
        self.root.destroy()
        new_root = tk.Tk() 
        obj = h.Personalisation(new_root) 
        new_root.mainloop()  
    

    def __init__(self):
        self.root = Tk()
        self.root.title("Picture")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="#fff")#
        self.root.resizable(width=False, height=False)

        window_width = 925
        window_height = 500
        center_window(self.root, window_width, window_height)  # Ensure this function is defined in centerwindow.py


        self.img = PhotoImage(file="/Users/akshsaini/Documents/PYproject//login.png")
        Label(self.root, image=self.img, bg="white").place(x=50, y=50)

        
        self.title=Label(text="Meet the better you",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light", 28, "bold"))
        self.title.place(x=520,y=40)

        self.label=Label(text="Enjoy  your  journey  of  becomming  a  finer  version  of  you", fg="steel blue",bg="white",font=("Microsoft YaHei UI Light", 12))
        self.label.place(x=480,y=85)

        self.label1=Label(text=" *   Plan daily routine with a habbit list", fg="slate grey",bg="white",font=("Microsoft YaHei UI Light", 18))
        self.label1.place(x=495,y=140)
        
        self.label2=Label(text=" *   regulate your life with smart reminders", fg="slate grey",bg="white",font=("Microsoft YaHei UI Light", 18))
        self.label2.place(x=495,y=190)

        self.label3=Label(text=" *   Enhance your academic scores", fg="slate grey",bg="white",font=("Microsoft YaHei UI Light", 18))
        self.label3.place(x=495,y=240)

        self.label4=Label(text=" *   Keep your streak and consolidate results", fg="slate grey",bg="white",font=("Microsoft YaHei UI Light", 18))
        self.label4.place(x=495,y=290)

        self.but1 = Button(text="Start now", bg="white", fg="#57a1f8",font=(16), border=0)
        self.but1.place(x=570, y=380, width=200, height=40)
        self.but1.bind("<Button-1>",self.button)

        self.root.mainloop()  # Start the Tkinter main loop

# To create an instance of the Personalise class
#if __name__ == "__main__":
    #app = Personalise()