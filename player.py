import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.title("Music Player")
root.geometry("540x700+690+0")
root.configure(background='white')
root.resizable(False, False)
mixer.init()

# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()



image_icon = PhotoImage(file="logo1.png")
root.iconphoto(False, image_icon)


frameCnt =30
frames = [PhotoImage(file='aa1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)


image1 = Image.open("play.png")
image1 = image1.resize((93, 50))
image2 = Image.open("stop.png")
image2 = image2.resize((85, 50))
image3 = Image.open("unpause.png")
image3 = image3.resize((100, 45))
image4 = Image.open("pause.png")
image4 = image4.resize((120, 50))

ButtonPlay = ImageTk.PhotoImage(image1)
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 45, width =42,
       command=PlayMusic).place(x=285, y=542)


ButtonStop = ImageTk.PhotoImage(image2)
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height = 42, width =42,
       command=mixer.music.stop).place(x=180, y=542)

Buttonvolume = ImageTk.PhotoImage(image3)
Button(root, image=Buttonvolume, bg="#FFFFFF", bd=0, height = 42, width =42,
       command=mixer.music.unpause).place(x=70, y=542)

ButtonPause = ImageTk.PhotoImage(image4)
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height = 42, width =42,
       command=mixer.music.pause).place(x=395, y=542)
     

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=110)



Button(root, text="Browse", wraplength=4, width=4, height=6, font=("calibri",
      12, "bold"), fg="purple", bg="pink", command=AddMusic).place(x=489, y=570)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="pink", fg="black", selectbackground="purple", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)


root.mainloop()