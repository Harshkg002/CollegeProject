from tkinter import *
from PIL import Image,ImageTk
from playsound import playsound
import pygame
from centerwindow import *


class pic():

    def nxtpage(self):

        import loginpg as p
        self.root.destroy()
        p.login()

    def __init__(self):
        self.root = Tk()
        self.root.title("Picture")
        self.root.geometry("925x500+300+200")
        self.root.resizable(width=False,height=False)

        self.main_frame = Frame(self.root,bg="white")
        self.main_frame.pack(fill=BOTH,expand=True)
        self.main_frame.columnconfigure(0,weight=1)
        self.main_frame.rowconfigure(0,weight=1)


        window_width=925
        window_height=500
        center_window(self.root,window_width,window_height)

        self.image_obj=ImageTk.PhotoImage(Image.open("/Users/akshsaini/Documents/PYproject/degreebee.jpg"))
        self.label_img=Label(self.main_frame,image=self.image_obj,bg="white")
        self.label_img.grid(column=0,row=0)


        self.root.after(3000,self.nxtpage)
        pygame.mixer.init()
        pygame.mixer.music.load("/Users/akshsaini/Documents/PYproject/welcome.mp3")
        pygame.mixer.music.play()


        self.root.mainloop()

obj=pic()




