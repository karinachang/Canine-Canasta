from tkinter import *
from pillow import ImageTk, Image

class Card():
    def __init__(self, number, suit, fullImg = None, topImg = None):
        self.number = number
        self.suit = suit
        self.fullImg = fullImg
        self.topImg = topImg

    @property
    def fullImg(self):
        return self._fullImg
    @fullImg.setter
    def fullImg(self, value):
        self._fullImg = value


AceSpades = Card(1, "spades", "blankbase.jpg")

window = Tk()
WIDTH = 1000
HEIGHT = 800

img = ImageTK.PhotoImage(Image.open(file=AceSpades.fullImg))
l1 = Label(window, width = WIDTH, height = HEIGHT,image = img)
l1.pack(side=LEFT)

l2 = Label(window, text = "Another label")
l2.pack(side=RIGHT)






window.title("Test")
window.mainloop()
