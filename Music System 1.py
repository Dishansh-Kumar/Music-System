from pygame import mixer
from tkinter import *
from tkinter import filedialog as fd
import os

def playsong():
    # Displaying Selected Song title
    track.set(Playlist.get(ACTIVE))
    # Loading Selected Song
    mixer.music.load(Playlist.get(ACTIVE))
    # Playing Selected Song
    mixer.music.play()
    status.set("Now Playing")



def stopsong():
    status.set("Stopped")
    # Stopped Song
    mixer.music.stop()


def pausesong():
    status.set("Paused")
    # Paused Song
    mixer.music.pause()


def unpausesong():
    status.set("Resume")
    # Playing back Song
    mixer.music.unpause()


def Next():
    # to get the selected song index
    next_one = Playlist.curselection()
    # to get the next song index
    next_one = next_one[0] + 1
    # to get the next song
    temp = Playlist.get(next_one)
    mixer.music.load(temp)
    mixer.music.play()
    Playlist.selection_clear(0, END)
    # activate newsong
    Playlist.activate(next_one)
    # set the next song
    Playlist.selection_set(next_one)
    # Displaying Status
    track.set(Playlist.get(ACTIVE))
    status.set("Now Playing")


def Prev():
    # to get the selected song index
    Prev_one = Playlist.curselection()
    # to get the Prev song index
    Prev_one = Prev_one[0] - 1
    # to get the Prev song
    temp = Playlist.get(Prev_one)
    mixer.music.load(temp)
    mixer.music.play()
    Playlist.selection_clear(0, END)
    # activate newsong
    Playlist.activate(Prev_one)
    # set the Prev song
    Playlist.selection_set(Prev_one)
    # Displaying Status
    track.set(Playlist.get(ACTIVE))
    status.set("Now Playing")


def myfunc():
    os.chdir(fd.askdirectory())
    songs = os.listdir()
    for song in songs:
        Playlist.insert(END, song)


root = Tk()
root.title("Music Player")
root.geometry("900x500")
root.resizable(False, False)
# Initiating Pygame Mixer
mixer.init()
# Declaring track Variable
track = StringVar()
# Declaring Status Variable
status = StringVar()
# Creating Track Frame for Song label & status label
trackframe = LabelFrame(root, text="Song Track", font=("times new roman", 15, "bold"), bg="Black",
                        fg="white", bd=5, relief=GROOVE)
trackframe.place(x=0, y=0, width=600, height=400)
# Inserting Song Track Label

songtrack = Label(trackframe, textvariable=track, width=30, font=("Arial",20),
                  bg="Black", fg="gold").grid(row=0, column=0,padx = 20)

photo = PhotoImage(file="music.gif")
label = Label(trackframe, songtrack, image=photo)
label.grid(row=1, padx=80)
# Inserting Status Label.
trackstatus = Label(trackframe, textvariable=status, font=("Arial", 24), bg="Black",
                    fg="gold").grid(row=10, column=0, padx=5, pady=20)

Mainmenu = Menu(root)
m1 = Menu(Mainmenu, tearoff=0)
m1.add_command(label="Add Songs", command=myfunc)
root.config(menu=Mainmenu)
Mainmenu.add_cascade(label="File", menu=m1)
Playlist = Listbox(root, selectbackground="gold", selectmode=SINGLE,
                   font=("helvetica", 12, "bold"), bg="Black",
                   width=30, fg="White", bd=5, height=30, relief=GROOVE)
Playlist.pack(side=RIGHT)
buttonframe = LabelFrame(root, text="Panel", font=("Arial", 15, "bold"), bg="Black", fg="White", bd=5, relief=GROOVE)
buttonframe.place(x=0, y=400, width=600, height=100)

playbtn = Button(buttonframe, text="PLAY", command=playsong, width=6, height=1, font=("Arial", 15, "bold"), fg="White",
                 bg="Black").grid(
    row=0, column=0, padx=10, pady=5)
# Inserting Pause Button
pausebtn = Button(buttonframe, text="PAUSE", command=pausesong, width=6, height=1, font=("Arial", 15, "bold"),
                  fg="White",
                  bg="black").grid(row=0, column=1, padx=10, pady=5)
# Inserting Unpause Button
unpausebtn = Button(buttonframe, text="RESUME", command=unpausesong, width=7, height=1,
                    font=("Arial", 15, "bold"), fg="White", bg="black").grid(row=0, column=2, padx=10, pady=5)
# Inserting Stop Button
stopbtn = Button(buttonframe, text="STOP", command=stopsong, width=6, height=1,
                 font=("Arial", 15, "bold"), fg="White", bg="black").grid(row=0, column=3, padx=5, pady=5)
nextbtn = Button(buttonframe, text="NEXT", command=Next, width=6, height=1,
                 font=("Arial", 15, "bold"), fg="White", bg="black").grid(row=0, column=4, padx=5, pady=5)
Prevbtn = Button(buttonframe, text="Prev", command=Prev, width=6, height=1,
                 font=("Arial", 15, "bold"), fg="White", bg="Black").grid(row=0, column=5, padx=5, pady=5)
root.mainloop()
