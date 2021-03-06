import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *
from mutagen.id3 import ID3
root=Tk()
root.minsize(300,300)

#songs array
listofsongs=[]
realnames=[]
index=0
v=StringVar()
songlabel=Label(root,textvariable=v,width=35)


def nextsong(event):
    global index
    global songname
    index+=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def previoussong(event):
    global index
    global songname
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    return songname

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    return songname

def directorychooser():
    directory=askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir=os.path.realpath(files)
            audio=ID3(realdir)
            realnames.append(audio["TIT2"].text[0])
            Music.append(files)
    

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

label=Label(root, text="Music Player")
label.pack()

realnames.reverse()

listbox=Listbox(root)
listbox.pack()

listofsongs.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()

nextbutton=Button(root,text="Next Song")
nextbutton.pack()

previousbutton=Button(root,text="Previous Song")
previousbutton.pack()

stopbutton=Button(root,text='Stop Song')
stopbutton.pack()

#Button-1 means left click
#Button-2 means mid click
#Button-3 means right click

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
root.mainloop()