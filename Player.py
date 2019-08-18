#import modules
import tkinter as tkr
from tkinter import filedialog;
import pygame
import os
import sys


#create window and frame
player =  tkr.Tk()


#adding RGB scheme 
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 


#change title and sizze of window
player.title("Audio PLayer")
player.geometry("250x340")
player.configure(bg =  _from_rgb((44, 44, 44)))


#os checker (now we don't need it)
'''
your_os = sys.platform
print(os)
'''


#going to playlist folder (depending on system)
home = os.path.expanduser("~")
os.chdir(home)

songlist = os.listdir()
print(songlist)


#playlist input
playlist = tkr.Listbox(player, highlightcolor = "blue", selectmode = tkr.SINGLE, bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1


#volume input
VolumeLevel = tkr.Scale(player, from_ = 1.0, to_ = 100.0, orient = tkr.HORIZONTAL, resolution = 1.0)
VolumeLevel.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))


#PyGame init
pygame.init()
pygame.mixer.init()


#add commands
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get() / 100)
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_volume(VolumeLevel.get() / 100)
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())

def Browse():
    global songlist, playlist
    os.chdir(filedialog.askdirectory())
    
    print(songlist, playlist )
    for i in songlist:
        playlist.delete(0)

    songlist = os.listdir()
    print(songlist)
    for item in songlist:
        pos = 0
        playlist.insert(pos, item)
        pos += 1


#add buttons
ButtStop = tkr.Button(player, width = 15, height = 1, text = "STOP", command = ExitPlayer) 
ButtStop.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtPlay = tkr.Button(player, width = 15, height = 1, text = "PLAY", command = Play)
ButtPlay.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtPause = tkr.Button(player, width = 15, height = 1, text = "PAUSE", command = Pause) 
ButtPause.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtUnPause = tkr.Button(player, width = 15, height = 1, text = "UNPAUSE", command = UnPause)
ButtUnPause.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtBrowse = tkr.Button(player, width = 15, height = 1, text = "BROWSE", command = Browse)
ButtBrowse.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))


#song name
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)
songtitle.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))


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