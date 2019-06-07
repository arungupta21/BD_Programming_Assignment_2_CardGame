# -*- coding: utf-8 -*-

"""
Let's Play !

@author: Arun Gupta
"""
import random


class Card:
    strName = ""
    iTopSpeed = 0
    iEnginePower = 0
    iPrice = 0
    
    def __init__(self, Name, TopSpeed, Power, Price):
        self.strName = Name
        self.iTopSpeed = TopSpeed
        self.iEnginePower = Power
        self.iPrice = Price
        
    def ShowCardDetails(self):
        print("--------------CARD DETAILS--------------")
        print("Name of Car: " + self.strName)
        print("Top Speed: " + str(self.iTopSpeed))
        print("Engine Power: " + str(self.iEnginePower))
        print("Price: " + str(self.iPrice))
        print("----------------------------------------")
        

class Deck:
    
    def __init__(self):
        self.Cards = []
    
    def AddCard(self, argCard):
        self.Cards.append(argCard)
    
    

class Player:
    
    strName = ""
    iScore = 0
    myDeck = 0
    bGodSpellAvailable = 0
    bResurrectSpellAvailable = 0
    
    
    def __init__(self, name):
        self.strName = name
        self.myDeck = Deck()
        self.bGodSpellAvailable = 1
        self.bResurrectSpellAvailable = 1
        
        

        

def MakeCard(Name, TopSpeed, Power, Price):
    myCard = Card(Name, TopSpeed, Power, Price) 
    return myCard

def PrintPlayerStatus(argPlayer):
    print(("*****" + argPlayer.strName + "'s Status" + "*****").upper())
    print("Score: " + str(argPlayer.iScore))
    print("God Spell Available? : " + "Yes" if argPlayer.bGodSpellAvailable == 1 else "No")
    print("Resurrect Spell Available? : " + "Yes" if argPlayer.bResurrectSpellAvailable == 1 else "No")
    print("# Cards in hand: " + str(len(argPlayer.myDeck.Cards)))
    

    
# Define Players

Player1Name = input("Name of Player 1: ") 
Player2Name = input("Name of Player 2: ") 
        
P1 = Player(Player1Name)
P2 = Player(Player2Name)

CommonDeck = Deck() # Common Deck

# 1. Define the cards----------------------------------------------
# Cards for Player 1
P1.myDeck.AddCard(Card("Aston Martin Valkyrie", 250, 1185, 3250000))
P1.myDeck.AddCard(Card("Tesla Roadster ", 250, 1185, 1650000))
P1.myDeck.AddCard(Card("Saleen S7 Twin Turbo ", 248, 1175, 1904344))
P1.myDeck.AddCard(Card("W Motors Fenyr ", 248, 1175, 1940222))
P1.myDeck.AddCard(Card("Hennessey Venom F5", 301, 1426, 1600000))
P1.myDeck.AddCard(Card("McLaren F1 ", 241, 1142, 4455669))
P1.myDeck.AddCard(Card("SSC Ultimate Aero ", 256, 1213, 225000))
P1.myDeck.AddCard(Card("Koenigsegg Agera RS ", 278, 1317, 1850000))
P1.myDeck.AddCard(Card("Zenvo ST1 ", 233, 1104, 4434344))
P1.myDeck.AddCard(Card("Dauer 962 Le Mans ", 250, 1185, 1200000))

# Cards for Player 2
P2.myDeck.AddCard(Card("Bugatti Veyron Super Sport", 268, 1270, 1670000))
P2.myDeck.AddCard(Card("Porsche 9ff TR 1000 ", 243, 1151, 1500000))
P2.myDeck.AddCard(Card("Aston Martin One", 220, 1042, 1870000))
P2.myDeck.AddCard(Card("Pagani Huayra BC ", 238, 1128, 1343232))
P2.myDeck.AddCard(Card("Lotec Sirius ", 250, 1185, 3400000))
P2.myDeck.AddCard(Card("Zenvo TS1 GT ", 233, 730, 4322423))
P2.myDeck.AddCard(Card("TVR Cerbera ", 240, 1137, 1266773))
P2.myDeck.AddCard(Card("Ferrari Enzo ZXX EVOLUTION ", 242, 1147, 3244321))
P2.myDeck.AddCard(Card("Lamborghini Veneno ", 221, 1047, 4500000))
P2.myDeck.AddCard(Card("Koenigsegg CCR ", 242, 1147, 4309009))
#----------------------------------------------------------------


# 2. Shuffle the cards

# 3. Roll the dice to determine the player who starts the game
iPlayer1Dice = 0
iPlayer2Dice = 0

while iPlayer1Dice == iPlayer2Dice:
    iPlayer1Dice = random.randint(1,6)
    iPlayer2Dice = random.randint(1,6)
    
iTurn = 0

if iPlayer1Dice > iPlayer2Dice:
    iTurn = 1
    print("It's " + P1.strName + "'s turn \n")
else:
    iTurn = 2
    print("It's " + P2.strName + "'s turn \n")
    

# Continue playing until both the players have cards in hand
while(len(P1.myDeck.Cards) > 0 and len(P2.myDeck.Cards) > 0):
    
    # 4. Display the score and spell status of both players
    #Info of Player 1
    print("\n\n\n==============================================")
    print("==============================================")
    PrintPlayerStatus(P1)
    print("\n")
    
    #Info of Player 2
    PrintPlayerStatus(P2)
    print("\n")
    
    
    
    #Set Primary & Secondary Decks
    if iTurn == 1:
        PlayerWithTurn = P1
        SecondaryPlayer =  P2
    elif iTurn == 2:
        PlayerWithTurn = P2
        SecondaryPlayer =  P1
        
        
    DrawnCardOfPlayerWithTurn = PlayerWithTurn.myDeck.Cards[0]
        
        
    # Pick the cards from the top of the deck of the player having the turn
    if(len(PlayerWithTurn.myDeck.Cards) <= 0):
        print("No Card left in Primary Deck !!!")
    else:
        print("\n\n" + PlayerWithTurn.strName + "'s drawn card:")
        DrawnCardOfPlayerWithTurn.ShowCardDetails()
        
        
    
    # Allow the player to choose the characteristic that is supposedly the best one 
    print(PlayerWithTurn.strName + ", Make your choice for characteristic" )
    print(" (1) For Top Speed")
    print(" (2) Engine Power")
    print(" (3) Price")
    
    # Player in command chooses the characteristic
    choice = input("Choice: ") 
    
    choice = int(choice)
    
    
    DrawnCardOfSecondaryPlayer = SecondaryPlayer.myDeck.Cards[0]
    
    # Pick the cards from the top of the deck of the other player 
    if(len(SecondaryPlayer.myDeck.Cards) <= 0):
        print("No Card left in Primary Deck !!!")
    else:
        print("\n\n" + SecondaryPlayer.strName + "'s drawn card:")
        DrawnCardOfSecondaryPlayer.ShowCardDetails()
        
        
    #Determine who wins
    
    
    Characteristic1 = 0
    Characteristic2 = 0
    
    if(choice == 1):
        Characteristic1 = DrawnCardOfPlayerWithTurn.iTopSpeed 
        Characteristic2 = DrawnCardOfSecondaryPlayer.iTopSpeed 
        print("Inside if argChoice == 1:")
    
    elif(choice == 2):
        Characteristic1 = DrawnCardOfPlayerWithTurn.iEnginePower 
        Characteristic2 = DrawnCardOfSecondaryPlayer.iEnginePower
        print("Inside if argChoice == 2:")
    
    elif(choice == 3):
        Characteristic1 = DrawnCardOfPlayerWithTurn.iPrice 
        Characteristic2 = DrawnCardOfSecondaryPlayer.iPrice
        print("Inside if argChoice == 3:")
    
    
    print("characteristic of player 1: " + str(Characteristic1))
    print("characteristic of player 2: " + str(Characteristic2))
    
    print("choice: " + str(choice))
    
    
    if(Characteristic1 > Characteristic2):
        PlayerWithTurn.iScore += 1
        print(PlayerWithTurn.strName + " wins")
    else:
        SecondaryPlayer.iScore += 1
        print(SecondaryPlayer.strName + " wins")
            
    # Add the used cards onto the common deck        
    CommonDeck.Cards.append(PlayerWithTurn.myDeck.Cards[0])
    CommonDeck.Cards.append(SecondaryPlayer.myDeck.Cards[0])
        
    # Remove the played cards from each player's deck
    del PlayerWithTurn.myDeck.Cards[0]
    del SecondaryPlayer.myDeck.Cards[0]
    
    
    #Change the turn
    iTurn = 2 if iTurn == 1 else 1


print("\n\nGame concluded !!\n")

WinnerName = P1.strName if P1.iScore > P2.iScore else P2.strName

print("Final Scores:\n")
print(P1.strName+"'s Score: " + str(P1.iScore))
print(P2.strName+"'s Score: " + str(P2.iScore))

if(P1.iScore == P2.iScore):
    print("\nIt's a tie. No one is the winner")
else: 
   print("\nCongratulations " + WinnerName + ". You are the Winner of the game!!!\n")






