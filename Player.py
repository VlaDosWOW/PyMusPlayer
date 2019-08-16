#import modules
import tkinter as tkr
import pygame
import os


#create window and frame
player =  tkr.Tk()


#adding RGB scheme 
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 


#change title and sizze of window
player.title("Audio PLayer")
player.geometry("250x340")
player.configure(bg =  _from_rgb((44, 44, 44)))


#add playlist
os.chdir("/home/user/Desktop/projects/PyMusPlayer/Ignore data")
#print(os.getcwd)
songlist = os.listdir()


#volume input
VolumeLevel = tkr.Scale(player, from_ = 1.0, to_ = 100.0, orient = tkr.HORIZONTAL, resolution = 1.0)
VolumeLevel.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

#playlist input
playlist = tkr.Listbox(player, highlightcolor = "blue", selectmode = tkr.SINGLE, bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))
#print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1


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


#add buttons
ButtStop = tkr.Button(player, width = 15, height = 1, text = "STOP", command = ExitPlayer) 
ButtStop.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtPlay = tkr.Button(player, width = 15, height = 1, text = "PLAY", command = Play)
ButtPlay.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtPause = tkr.Button(player, width = 15, height = 1, text = "PAUSE", command = Pause) 
ButtPause.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtUnPause = tkr.Button(player, width = 15, height = 1, text = "UNPAUSE", command = UnPause)
ButtUnPause.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))
#song name
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)
songtitle.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))


#place widgets
songtitle.pack(side = "top", fill = 'x')

ButtPlay.pack(fill = "x")
ButtStop.pack(fill = "x")

ButtPause.pack(fill = "x")
ButtUnPause.pack(fill = "x")

VolumeLevel.pack(fill = 'x')

playlist.pack(fill = 'both', expand = 'yes')


#activate
player.mainloop()