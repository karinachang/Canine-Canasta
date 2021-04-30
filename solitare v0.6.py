from tkinter import *
from random import randint

deck1 = []
deck2 = []
deck3 = []
deck4 = []

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

def deckSetup():
    global deck1
    global deck2
    global deck3
    global deck4
    AceSpades = Card(1, "spades", "AceSpades.gif")
    AceHearts = Card(1, "hearts", "AceHearts.gif")
    TwoSpades = Card(2, "spades", "TwoSpades.gif")
    TwoHearts = Card(2, "hearts", "TwoHearts.gif")
    ThreeSpades = Card(3, "spades", "ThreeSpades.gif")
    ThreeHearts = Card(3, "hearts", "ThreeHearts.gif")
    FourSpades = Card(4, "spades", "FourSpades.gif")
    FourHearts = Card(4, "hearts", "FourHearts.gif")
    FiveSpades = Card(5, "spades", "FiveSpades.gif")
    FiveHearts = Card(5, "hearts", "FiveHearts.gif")
    SixSpades = Card(6, "spades", "SixSpades.gif")
    SixHearts = Card(6, "hearts", "SixHearts.gif")
    SevenSpades = Card(7, "spades", "SevenSpades.gif")
    SevenHearts = Card(7, "hearts", "SevenHearts.gif")
    EightSpades = Card(8, "spades", "EightSpades.gif")
    EightHearts = Card(8, "hearts", "EightHearts.gif")
    NineSpades = Card(9, "spades", "NineSpades.gif")
    NineHearts = Card(9, "hearts", "NineHearts.gif")
    TenSpades = Card(10, "spades", "TenSpades.gif")
    TenHearts = Card(10, "hearts", "TenHearts.gif")
    JackSpades = Card(11, "spades", "JackSpades.gif")
    JackHearts = Card(11, "hearts", "JackHearts.gif")
    QueenSpades = Card(12, "spades", "QueenSpades.gif")
    QueenHearts = Card(12, "hearts", "QueenHearts.gif")
    KingSpades = Card(13, "spades", "KingSpades.gif")
    KingHearts = Card(13, "hearts", "KingHearts.gif")


    deck1 = [AceSpades, AceHearts, TwoSpades, TwoHearts, ThreeSpades, ThreeHearts, FourSpades, FourHearts, FiveSpades, FiveHearts, SixSpades, SixHearts, SevenSpades, SevenHearts, EightSpades, EightHearts, NineSpades, NineHearts, TenSpades, TenHearts, JackSpades, JackHearts, QueenSpades, QueenHearts, KingSpades, KingHearts]
    deck2 = [AceSpades, AceHearts, TwoSpades, TwoHearts, ThreeSpades, ThreeHearts, FourSpades, FourHearts, FiveSpades, FiveHearts, SixSpades, SixHearts, SevenSpades, SevenHearts, EightSpades, EightHearts, NineSpades, NineHearts, TenSpades, TenHearts, JackSpades, JackHearts, QueenSpades, QueenHearts, KingSpades, KingHearts]
    deck3 = [AceSpades, AceHearts, TwoSpades, TwoHearts, ThreeSpades, ThreeHearts, FourSpades, FourHearts, FiveSpades, FiveHearts, SixSpades, SixHearts, SevenSpades, SevenHearts, EightSpades, EightHearts, NineSpades, NineHearts, TenSpades, TenHearts, JackSpades, JackHearts, QueenSpades, QueenHearts, KingSpades, KingHearts]
    deck4 = [AceSpades, AceHearts, TwoSpades, TwoHearts, ThreeSpades, ThreeHearts, FourSpades, FourHearts, FiveSpades, FiveHearts, SixSpades, SixHearts, SevenSpades, SevenHearts, EightSpades, EightHearts, NineSpades, NineHearts, TenSpades, TenHearts, JackSpades, JackHearts, QueenSpades, QueenHearts, KingSpades, KingHearts]
    
def rowSetup():
    global row1
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    row10 = []
    totalStock = []
    totalStock.extend(deck1)
    totalStock.extend(deck2)
    totalStock.extend(deck3)
    totalStock.extend(deck4)
    print(len(totalStock))
    for i in range(0, 5):
        x = randint(0,len(totalStock))
        row1.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock))
        row2.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock))
        row3.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock))
        row4.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 4):
        x = randint(0,len(totalStock))
        row5.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 4):
        x = randint(0,len(totalStock))
        row6.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 4):
        x = randint(0,len(totalStock))
        row7.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 4):
        x = randint(0,len(totalStock))
        row8.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 4):
        x = randint(0,len(totalStock))
        row9.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 4):
        x = randint(0,len(totalStock))
        row10.append(totalStock[x])
        del totalStock[x]
    print(len(totalStock))
    

deckSetup()        
rowSetup()


window = Tk()
WIDTH = 800
HEIGHT = 600

##img = PhotoImage(file=row1[1].fullImg)
##l1 = Label(window, width = WIDTH, height = HEIGHT,image = img)
##l1.pack(side=LEFT)
##
##
##window.title("Test")
##window.mainloop()
