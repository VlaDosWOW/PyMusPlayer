#import modules
import tkinter as tkr
import pygame
import os


#create window and frame
player =  tkr.Tk()
#frame_up


#adding RGB scheme 
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 


#change title and sizze of window
player.title("Audio PLayer")
player.geometry("250x340")
player.configure(bg = "grey")


#add playlist
os.chdir("/home/user/Desktop/projects/PyMusPlayer")
print(os.getcwd)
songlist = os.listdir()


#playlist input
playlist = tkr.Listbox(player, highlightcolor = "blue", selectmode = tkr.SINGLE)
print(songlist)
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

def ExitPlayer():
    pygame.mixer.music.stop()

#add buttons
ButtStop = tkr.Button(player, width = 15, height = 4, text = "STOP", command = ExitPlayer) 
ButtStop.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))

ButtPlay = tkr.Button(player, width = 15, height = 4, text = "PLAY", command = Play)
ButtPlay.config(bg = _from_rgb((44, 44, 44)) , fg = _from_rgb((225,225,225)), highlightbackground = _from_rgb((60,60,60)))


#song name
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)


#place widgets
songtitle.pack(side = "top", anchor = "s")
ButtStop.pack(side = "bottom", fill = "x")
ButtPlay.pack(side = "bottom", fill = "x")
playlist.pack(fill = 'both', expand = 'yes')


#activate
player.mainloop()
