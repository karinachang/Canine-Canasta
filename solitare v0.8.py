from tkinter import *
from random import randint

deck1 = []
deck2 = []
deck3 = []
deck4 = []

window = Tk()
WIDTH = 90
HEIGHT = 130

class Card():
    def __init__(self, number, suit, fullImg = None, selectedImg = None, Hidden = True, Selected = False, Chosen = False):
        self.number = number
        self.suit = suit
        self.fullImg = fullImg
        self.selectedImg = selectedImg
        self.Hidden = Hidden
        self.Selected = Selected
        self.Chosen = Chosen

    @property
    def fullImg(self):
        if(self.Hidden == True):
            return "blankbase.gif"
        elif(self.Selected == True):
            return self._selectedImg
        else:
            return self._fullImg
    @fullImg.setter
    def fullImg(self, value):
        self._fullImg = value
        
    @property
    def selectedImg(self):
        return self._selectedImg
    @selectedImg.setter
    def selectedImg(self, value):
        self._selectedImg = value
        
    @property
    def Hidden(self):
        return self._Hidden
    @Hidden.setter
    def Hidden(self, value):
        self._Hidden = value

    @property
    def Selected(self):
        return self._Selected
    @Selected.setter
    def Selected(self, value):
        self._Selected = value

    @property
    def Chosen(self):
        return self._Chosen
    @Chosen.setter
    def Chosen(self, value):
        self._Chosen = value

    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, value):
        self._number = value

def deckSetup():
    global deck1
    global deck2
    global deck3
    global deck4
    AceSpades = Card(1, "spades", "AceSpades.gif", "SelectedAceSpades.gif")
    AceHearts = Card(1, "hearts", "AceHearts.gif", "SelectedAceHearts.gif")
    TwoSpades = Card(2, "spades", "TwoSpades.gif", "SelectedTwoSpades.gif")
    TwoHearts = Card(2, "hearts", "TwoHearts.gif", "SelectedTwoHearts.gif")
    ThreeSpades = Card(3, "spades", "ThreeSpades.gif", "SelectedThreeSpades.gif")
    ThreeHearts = Card(3, "hearts", "ThreeHearts.gif", "SelectedThreeHearts.gif")
    FourSpades = Card(4, "spades", "FourSpades.gif", "SelectedFourSpades.gif")
    FourHearts = Card(4, "hearts", "FourHearts.gif", "SelectedFourHearts.gif")
    FiveSpades = Card(5, "spades", "FiveSpades.gif", "SelectedFiveSpades.gif")
    FiveHearts = Card(5, "hearts", "FiveHearts.gif", "SelectedFiveHearts.gif")
    SixSpades = Card(6, "spades", "SixSpades.gif", "SelectedSixSpades.gif")
    SixHearts = Card(6, "hearts", "SixHearts.gif", "SelectedSixHearts.gif")
    SevenSpades = Card(7, "spades", "SevenSpades.gif", "SelectedSevenSpades.gif")
    SevenHearts = Card(7, "hearts", "SevenHearts.gif", "SelectedSevenHearts.gif")
    EightSpades = Card(8, "spades", "EightSpades.gif", "SelectedEightSpades.gif")
    EightHearts = Card(8, "hearts", "EightHearts.gif", "SelectedEightHearts.gif")
    NineSpades = Card(9, "spades", "NineSpades.gif", "SelectedNineSpades.gif")
    NineHearts = Card(9, "hearts", "NineHearts.gif","SelectedNineHearts.gif")
    TenSpades = Card(10, "spades", "TenSpades.gif", "SelectedTenSpades.gif")
    TenHearts = Card(10, "hearts", "TenHearts.gif", "SelectedTenHearts.gif")
    JackSpades = Card(11, "spades", "JackSpades.gif", "SelectedJackSpades.gif")
    JackHearts = Card(11, "hearts", "JackHearts.gif", "SelectedJackHearts.gif")
    QueenSpades = Card(12, "spades", "QueenSpades.gif", "SelectedQueenSpades.gif")
    QueenHearts = Card(12, "hearts", "QueenHearts.gif", "SelectedQueenHearts.gif")
    KingSpades = Card(13, "spades", "KingSpades.gif", "SelectedKingSpades.gif")
    KingHearts = Card(13, "hearts", "KingHearts.gif", "SelectedKingHearts.gif")

    #To give every unique card a true/false hidden value I had to made every card in each deck unique instead
    #of generating one card of each type and using it 4 times. Annoying but it makes it 100x easier to keep
    #track of which card is supposed to be hidden
    AceSpades2 = Card(1, "spades", "AceSpades.gif", "SelectedAceSpades.gif")
    AceHearts2 = Card(1, "hearts", "AceHearts.gif", "SelectedAceHearts.gif")
    TwoSpades2 = Card(2, "spades", "TwoSpades.gif", "SelectedTwoSpades.gif")
    TwoHearts2 = Card(2, "hearts", "TwoHearts.gif", "SelectedTwoHearts.gif")
    ThreeSpades2 = Card(3, "spades", "ThreeSpades.gif", "SelectedThreeSpades.gif")
    ThreeHearts2 = Card(3, "hearts", "ThreeHearts.gif", "SelectedThreeHearts.gif")
    FourSpades2 = Card(4, "spades", "FourSpades.gif", "SelectedFourSpades.gif")
    FourHearts2 = Card(4, "hearts", "FourHearts.gif", "SelectedFourHearts.gif")
    FiveSpades2 = Card(5, "spades", "FiveSpades.gif", "SelectedFiveSpades.gif")
    FiveHearts2 = Card(5, "hearts", "FiveHearts.gif", "SelectedFiveHearts.gif")
    SixSpades2 = Card(6, "spades", "SixSpades.gif", "SelectedSixSpades.gif")
    SixHearts2 = Card(6, "hearts", "SixHearts.gif", "SelectedSixHearts.gif")
    SevenSpades2 = Card(7, "spades", "SevenSpades.gif", "SelectedSevenSpades.gif")
    SevenHearts2 = Card(7, "hearts", "SevenHearts.gif", "SelectedSevenHearts.gif")
    EightSpades2 = Card(8, "spades", "EightSpades.gif", "SelectedEightSpades.gif")
    EightHearts2 = Card(8, "hearts", "EightHearts.gif", "SelectedEightHearts.gif")
    NineSpades2 = Card(9, "spades", "NineSpades.gif", "SelectedNineSpades.gif")
    NineHearts2 = Card(9, "hearts", "NineHearts.gif","SelectedNineHearts.gif")
    TenSpades2 = Card(10, "spades", "TenSpades.gif", "SelectedTenSpades.gif")
    TenHearts2 = Card(10, "hearts", "TenHearts.gif", "SelectedTenHearts.gif")
    JackSpades2 = Card(11, "spades", "JackSpades.gif", "SelectedJackSpades.gif")
    JackHearts2 = Card(11, "hearts", "JackHearts.gif", "SelectedJackHearts.gif")
    QueenSpades2 = Card(12, "spades", "QueenSpades.gif", "SelectedQueenSpades.gif")
    QueenHearts2 = Card(12, "hearts", "QueenHearts.gif", "SelectedQueenHearts.gif")
    KingSpades2 = Card(13, "spades", "KingSpades.gif", "SelectedKingSpades.gif")
    KingHearts2 = Card(13, "hearts", "KingHearts.gif", "SelectedKingHearts.gif")

    AceSpades3 = Card(1, "spades", "AceSpades.gif", "SelectedAceSpades.gif")
    AceHearts3 = Card(1, "hearts", "AceHearts.gif", "SelectedAceHearts.gif")
    TwoSpades3 = Card(2, "spades", "TwoSpades.gif", "SelectedTwoSpades.gif")
    TwoHearts3 = Card(2, "hearts", "TwoHearts.gif", "SelectedTwoHearts.gif")
    ThreeSpades3 = Card(3, "spades", "ThreeSpades.gif", "SelectedThreeSpades.gif")
    ThreeHearts3 = Card(3, "hearts", "ThreeHearts.gif", "SelectedThreeHearts.gif")
    FourSpades3 = Card(4, "spades", "FourSpades.gif", "SelectedFourSpades.gif")
    FourHearts3 = Card(4, "hearts", "FourHearts.gif", "SelectedFourHearts.gif")
    FiveSpades3 = Card(5, "spades", "FiveSpades.gif", "SelectedFiveSpades.gif")
    FiveHearts3 = Card(5, "hearts", "FiveHearts.gif", "SelectedFiveHearts.gif")
    SixSpades3 = Card(6, "spades", "SixSpades.gif", "SelectedSixSpades.gif")
    SixHearts3 = Card(6, "hearts", "SixHearts.gif", "SelectedSixHearts.gif")
    SevenSpades3 = Card(7, "spades", "SevenSpades.gif", "SelectedSevenSpades.gif")
    SevenHearts3 = Card(7, "hearts", "SevenHearts.gif", "SelectedSevenHearts.gif")
    EightSpades3 = Card(8, "spades", "EightSpades.gif", "SelectedEightSpades.gif")
    EightHearts3 = Card(8, "hearts", "EightHearts.gif", "SelectedEightHearts.gif")
    NineSpades3 = Card(9, "spades", "NineSpades.gif", "SelectedNineSpades.gif")
    NineHearts3 = Card(9, "hearts", "NineHearts.gif","SelectedNineHearts.gif")
    TenSpades3 = Card(10, "spades", "TenSpades.gif", "SelectedTenSpades.gif")
    TenHearts3 = Card(10, "hearts", "TenHearts.gif", "SelectedTenHearts.gif")
    JackSpades3 = Card(11, "spades", "JackSpades.gif", "SelectedJackSpades.gif")
    JackHearts3 = Card(11, "hearts", "JackHearts.gif", "SelectedJackHearts.gif")
    QueenSpades3 = Card(12, "spades", "QueenSpades.gif", "SelectedQueenSpades.gif")
    QueenHearts3 = Card(12, "hearts", "QueenHearts.gif", "SelectedQueenHearts.gif")
    KingSpades3 = Card(13, "spades", "KingSpades.gif", "SelectedKingSpades.gif")
    KingHearts3 = Card(13, "hearts", "KingHearts.gif", "SelectedKingHearts.gif")

    AceSpades4 = Card(1, "spades", "AceSpades.gif", "SelectedAceSpades.gif")
    AceHearts4 = Card(1, "hearts", "AceHearts.gif", "SelectedAceHearts.gif")
    TwoSpades4 = Card(2, "spades", "TwoSpades.gif", "SelectedTwoSpades.gif")
    TwoHearts4 = Card(2, "hearts", "TwoHearts.gif", "SelectedTwoHearts.gif")
    ThreeSpades4 = Card(3, "spades", "ThreeSpades.gif", "SelectedThreeSpades.gif")
    ThreeHearts4 = Card(3, "hearts", "ThreeHearts.gif", "SelectedThreeHearts.gif")
    FourSpades4 = Card(4, "spades", "FourSpades.gif", "SelectedFourSpades.gif")
    FourHearts4 = Card(4, "hearts", "FourHearts.gif", "SelectedFourHearts.gif")
    FiveSpades4 = Card(5, "spades", "FiveSpades.gif", "SelectedFiveSpades.gif")
    FiveHearts4 = Card(5, "hearts", "FiveHearts.gif", "SelectedFiveHearts.gif")
    SixSpades4 = Card(6, "spades", "SixSpades.gif", "SelectedSixSpades.gif")
    SixHearts4 = Card(6, "hearts", "SixHearts.gif", "SelectedSixHearts.gif")
    SevenSpades4 = Card(7, "spades", "SevenSpades.gif", "SelectedSevenSpades.gif")
    SevenHearts4 = Card(7, "hearts", "SevenHearts.gif", "SelectedSevenHearts.gif")
    EightSpades4 = Card(8, "spades", "EightSpades.gif", "SelectedEightSpades.gif")
    EightHearts4 = Card(8, "hearts", "EightHearts.gif", "SelectedEightHearts.gif")
    NineSpades4 = Card(9, "spades", "NineSpades.gif", "SelectedNineSpades.gif")
    NineHearts4 = Card(9, "hearts", "NineHearts.gif","SelectedNineHearts.gif")
    TenSpades4 = Card(10, "spades", "TenSpades.gif", "SelectedTenSpades.gif")
    TenHearts4 = Card(10, "hearts", "TenHearts.gif", "SelectedTenHearts.gif")
    JackSpades4 = Card(11, "spades", "JackSpades.gif", "SelectedJackSpades.gif")
    JackHearts4 = Card(11, "hearts", "JackHearts.gif", "SelectedJackHearts.gif")
    QueenSpades4 = Card(12, "spades", "QueenSpades.gif", "SelectedQueenSpades.gif")
    QueenHearts4 = Card(12, "hearts", "QueenHearts.gif", "SelectedQueenHearts.gif")
    KingSpades4 = Card(13, "spades", "KingSpades.gif", "SelectedKingSpades.gif")
    KingHearts4 = Card(13, "hearts", "KingHearts.gif", "SelectedKingHearts.gif")


    deck1 = [AceSpades, AceHearts, TwoSpades, TwoHearts, ThreeSpades, ThreeHearts, FourSpades, FourHearts, FiveSpades, FiveHearts, SixSpades, SixHearts, SevenSpades, SevenHearts, EightSpades, EightHearts, NineSpades, NineHearts, TenSpades, TenHearts, JackSpades, JackHearts, QueenSpades, QueenHearts, KingSpades, KingHearts]
    deck2 = [AceSpades2, AceHearts2, TwoSpades2, TwoHearts2, ThreeSpades2, ThreeHearts2, FourSpades2, FourHearts2, FiveSpades2, FiveHearts2, SixSpades2, SixHearts2, SevenSpades2, SevenHearts2, EightSpades2, EightHearts2, NineSpades2, NineHearts2, TenSpades2, TenHearts2, JackSpades2, JackHearts2, QueenSpades2, QueenHearts2, KingSpades2, KingHearts2]
    deck3 = [AceSpades3, AceHearts3, TwoSpades3, TwoHearts3, ThreeSpades3, ThreeHearts3, FourSpades3, FourHearts3, FiveSpades3, FiveHearts3, SixSpades3, SixHearts3, SevenSpades3, SevenHearts3, EightSpades3, EightHearts3, NineSpades3, NineHearts3, TenSpades3, TenHearts3, JackSpades3, JackHearts3, QueenSpades3, QueenHearts3, KingSpades3, KingHearts3]
    deck4 = [AceSpades4, AceHearts4, TwoSpades4, TwoHearts4, ThreeSpades4, ThreeHearts4, FourSpades4, FourHearts4, FiveSpades4, FiveHearts4, SixSpades4, SixHearts4, SevenSpades4, SevenHearts4, EightSpades4, EightHearts4, NineSpades4, NineHearts4, TenSpades4, TenHearts4, JackSpades4, JackHearts4, QueenSpades4, QueenHearts4, KingSpades4, KingHearts4]
    
def rowSetup():
    global row1
    global row2
    global row3
    global row4
    global row5
    global row5
    global row6
    global row7
    global row8
    global row9
    global row10
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
    for i in range(0, 6):
        x = randint(0,len(totalStock)) - 1
        row1.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 6):
        x = randint(0,len(totalStock)) - 1
        row2.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 6):
        x = randint(0,len(totalStock)) - 1
        row3.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 6):
        x = randint(0,len(totalStock)) - 1
        row4.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock)) - 1
        row5.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock)) - 1
        row6.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock)) - 1
        row7.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock)) - 1
        row8.append(totalStock[x])
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock)) - 1
        row9.append(totalStock[x]) 
        del totalStock[x]
    for i in range(0, 5):
        x = randint(0,len(totalStock)) - 1
        row10.append(totalStock[x])
        del totalStock[x]
    row1[5].Hidden = False
    row2[5].Hidden = False
    row3[5].Hidden = False
    row4[5].Hidden = False
    row5[4].Hidden = False
    row6[4].Hidden = False
    row7[4].Hidden = False
    row8[4].Hidden = False
    row9[4].Hidden = False
    row10[4].Hidden = False
    for i in range(len(totalStock)):
        totalStock[i].Hidden = False
    
 
    
def runGame():
    deckSetup()        
    rowSetup()
    selection = [row1, 5]
    selectRender(selection)
    render()
    gameStatus = "InProgress"

    
    rowList = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]
    track = 0

    picked = [None, None]

    while(gameStatus == "InProgress"):
        move = input("Move")
        if(move == "a"):
            try:
                deSelect(selection)
                if(len(rowList[track]) != len(rowList[track - 1])):
                   selection[1] = len(rowList[track - 1]) - 1
                track -= 1
                selection[0] = rowList[track]
                selectRender(selection)
                render()
            except:
                pass
        elif(move == "d"):
            try:
                deSelect(selection)
                if(len(rowList[track]) != len(rowList[track + 1])):
                   selection[1] = len(rowList[track + 1]) - 1
                track += 1
                selection[0] = rowList[track]
                selectRender(selection)
                render()
            except:
                pass
        elif(move == " "):
            if(picked[0] == None):
                selectRender(selection)
                selection[0][selection[1]].Chosen = True
                picked[0] = selection[0]
                picked[1] = selection[1]
            else:
                picked[0][picked[1]].Chosen = False
                deSelect(picked)
                if(picked[0][picked[1]].number == selection[0][selection[1]].number - 1):
                    selection[0].append(picked[0][picked[1]])
                    del picked[0][picked[1]]
                changeRender(picked[0])
                picked[0] = None
                render()
        elif(move == "w"):
            if(selection[0][selection[1]-1].Hidden == False):
                selection[1] -= 1
                selectRender(selection)
                render()
            else:
                print("a")
                pass
                
                
            
            
        
            
            
    


    
    endPile1 = []
    endPile2 = []
    endPile3 = []
    endPile4 = []
    endPile5 = []
    endPile6 = []
    endPile7 = []
    endPile8 = []

def render():
    # Canvas for some reason requires every image to be hosted by a unique string. So to have a dynamic number of cards in a row I had to do this. Im sure there is a better way
    # but I dont have the time to work one out and the code runs with this so it will have to stay.
    row1img= ["r11", "r12", "r13", "r14", "r15", "r16", "r17", "r18", "r19", "r110", "r111", "r112", "r113", "r114", "r115", "r116", "r117", "r118", "r119", "r120"]
    row2img= ["r21", "r22", "r23", "r24", "r25", "r26", "r27", "r28", "r29", "r210", "r211", "r212", "r213", "r214", "r215", "r216", "r217", "r218", "r219", "r220"]
    row3img= ["r31", "r32", "r33", "r34", "r35", "r36", "r37", "r38", "r39", "r310", "r311", "r312", "r313", "r314", "r315", "r316", "r317", "r318", "r319", "r320"]
    row4img= ["r41", "r42", "r43", "r44", "r45", "r46", "r47", "r48", "r49", "r410", "r411", "r412", "r413", "r414", "r415", "r416", "r417", "r418", "r419", "r420"]
    row5img= ["r51", "r52", "r53", "r54", "r55", "r56", "r57", "r58", "r59", "r510", "r511", "r512", "r513", "r514", "r515", "r516", "r517", "r518", "r519", "r520"]
    row6img= ["r61", "r62", "r63", "r64", "r65", "r66", "r67", "r68", "r69", "r610", "r611", "r612", "r613", "r614", "r615", "r616", "r617", "r618", "r619", "r620"]
    row7img= ["r71", "r72", "r73", "r74", "r75", "r76", "r77", "r78", "r79", "r710", "r711", "r712", "r713", "r714", "r715", "r716", "r717", "r718", "r719", "r720"]
    row8img= ["r81", "r82", "r83", "r84", "r85", "r86", "r87", "r88", "r89", "r810", "r811", "r812", "r813", "r814", "r815", "r816", "r817", "r818", "r819", "r820"]
    row9img= ["r91", "r92", "r93", "r94", "r95", "r96", "r97", "r98", "r99", "r910", "r911", "r912", "r913", "r914", "r915", "r916", "r917", "r918", "r919", "r920"]
    row10img= ["r101", "r102", "r103", "r104", "r105", "r106", "r107", "r108", "r109", "r1010", "r1011", "r1012", "r1013", "r1014", "r1015", "r1016", "r1017", "r1018", "r1019", "r1020"]

    for i in range(len(row1)):
        row1img[i] = PhotoImage(file=row1[i].fullImg)
        r1 = Label(window, width = WIDTH, height = HEIGHT,image = row1img[i])
        r1.grid(row = i, column = 0, sticky = NS)
        
    for i in range(len(row2)):
        row2img[i] = PhotoImage(file=row2[i].fullImg)
        r2 = Label(window, width = WIDTH, height = HEIGHT,image = row2img[i])
        r2.grid(row = i, column = 1, sticky = NS)
    for i in range(len(row3)):
        row3img[i] = PhotoImage(file=row3[i].fullImg)
        r3 = Label(window, width = WIDTH, height = HEIGHT,image = row3img[i])
        r3.grid(row = i, column = 2, sticky = NS)
    for i in range(len(row4)):
        row4img[i] = PhotoImage(file=row4[i].fullImg)
        r4 = Label(window, width = WIDTH, height = HEIGHT,image = row4img[i])
        r4.grid(row = i, column = 3, sticky = NS)
    for i in range(len(row5)):
        row5img[i] = PhotoImage(file=row5[i].fullImg)
        r5 = Label(window, width = WIDTH, height = HEIGHT,image = row5img[i])
        r5.grid(row = i, column = 4, sticky = NS)
    for i in range(len(row6)):
        row6img[i] = PhotoImage(file=row6[i].fullImg)
        r6 = Label(window, width = WIDTH, height = HEIGHT,image = row6img[i])
        r6.grid(row = i, column = 5, sticky = NS)
    for i in range(len(row7)):
        row7img[i] = PhotoImage(file=row7[i].fullImg)
        r7 = Label(window, width = WIDTH, height = HEIGHT,image = row7img[i])
        r7.grid(row = i, column = 6, sticky = NS)
    for i in range(len(row8)):
        row8img[i] = PhotoImage(file=row8[i].fullImg)
        r8 = Label(window, width = WIDTH, height = HEIGHT,image = row8img[i])
        r8.grid(row = i, column = 7, sticky = NS)
    for i in range(len(row9)):
        row9img[i] = PhotoImage(file=row9[i].fullImg)
        r9 = Label(window, width = WIDTH, height = HEIGHT,image = row9img[i])
        r9.grid(row = i, column = 8, sticky = NS)
    for i in range(len(row10)):
        row10img[i] = PhotoImage(file=row10[i].fullImg)
        r10 = Label(window, width = WIDTH, height = HEIGHT,image = row10img[i])
        r10.grid(row = i, column = 9, sticky = NS)

    window.title("Test")
    window.update()
    
    

def deSelect(selection):
    if(selection[0][selection[1]].Chosen == False):
        selection[0][selection[1]].Selected = False
    else:
        pass

def selectRender(selection):
    selection[0][selection[1]].Selected = True

    

def changeRender(row):
    x = len(row)
    row[x-1].Hidden = False

runGame()





##window.title("Test")
##window.mainloop()
##
