from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer

mixer.init()

root = Tk()
root.geometry("1000x500")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("7qwgd8.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    mixer.music.load("JARVIS START UP.mp3")
    mixer.music.play()

    frames = ImageSequence.Iterator(img)
    frames = [frame.resize((1000, 500)) for frame in frames]
    frames = [ImageTk.PhotoImage(frame) for frame in frames]

    def update_image(frame):
        lbl.config(image=frame)
        root.update()

    for frame in frames:
        update_image(frame)
        time.sleep(0.05)
    root.destroy()


play_gif()
root.mainloop()
