#import modules
import tkinter as tkr
import tkinter.filedialog
import pygame
import os
import sys


#create window and frame
player =  tkr.Tk()


#change title and sizze of window
player.title("Audio PLayer")
player.geometry("250x340")
player.configure(bg =  '#2c2c2c')


#os checker (now we don't need it)
'''
your_os = sys.platform
print(os)
'''


#going to playlist folder
home = os.path.expanduser("~")
os.chdir(home)

songlist = os.listdir()
#print(songlist)


#playlist input
playlist = tkr.Listbox(player, highlightcolor = "blue", selectmode = tkr.SINGLE, bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')
for item in songlist:
    if item.endswith('.mp3'):
        pos = 0
        playlist.insert(pos, item)
        pos += 1


#creating iist for music folders
MusFolders = []


#volume input
VolumeLevel = tkr.Scale(player, from_ = 1.0, to_ = 100.0, orient = tkr.HORIZONTAL, resolution = 1.0)
VolumeLevel.config(bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')
VolumeLevel.set(30)

#PyGame init
pygame.mixer.init()


#add commands
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get() / 100)
    pygame.mixer.music.get_volume()

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_volume(VolumeLevel.get() / 100)
    pygame.mixer.music.get_volume()
    VolumeLevel.get()

def Browse():
    global songlist, playlist, MusFolders
    os.chdir(tkinter.filedialog.askdirectory())
    
    print(MusFolders)
    MusFolders.append(os.getcwd())
    print(MusFolders)

    print(songlist)
    for songlist in songlist:
        playlist.delete(0)

    songlist = os.listdir()
    print(songlist)
    for item in songlist:
        if item.endswith('.mp3'):
            pos = 0
            playlist.insert(pos, item)
            pos += 1


#add buttons
ButtStop = tkr.Button(player, width = 15, height = 1, text = "STOP", command = ExitPlayer) 
ButtStop.config(bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')

ButtPlay = tkr.Button(player, width = 15, height = 1, text = "PLAY", command = Play)
ButtPlay.config(bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')

ButtPause = tkr.Button(player, width = 15, height = 1, text = "PAUSE", command = Pause) 
ButtPause.config(bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')

ButtUnPause = tkr.Button(player, width = 15, height = 1, text = "UNPAUSE", command = UnPause)
ButtUnPause.config(bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')

ButtBrowse = tkr.Button(player, width = 15, height = 1, text = "BROWSE", command = Browse)
ButtBrowse.config(bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')


#song name
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)
songtitle.config(bg = '#2c2c2c' , fg = '#ffffff', highlightbackground = '#3c3c3c')


#place widgets
songtitle.pack(fill = 'x')

ButtPlay.pack(fill = "x")
ButtStop.pack(fill = "x")

ButtPause.pack(fill = "x")
ButtUnPause.pack(fill = "x")

VolumeLevel.pack(fill = 'x')

ButtBrowse.pack(fill = 'x')

playlist.pack(fill = 'both', expand = 'yes')


#activate
player.mainloop()
