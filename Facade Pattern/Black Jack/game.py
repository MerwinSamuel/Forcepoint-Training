
from player import Player
from deck import Deck
import random

class Game():
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name,0)
        self.player2 = Player(player2Name,0)
        self.deck = Deck.createDeck()
        self.turn = 1
        self.isLastSkipped = False

    def displayScores(self):
        print(f"Player 1 {self.player1.points}")
        print(f"Player 2 {self.player2.points}")
        print("\n")

    def endGame(self):
        if self.player1.points>self.player2.points:
            print("Player1 wins")
        elif self.player1.points<self.player2.points:
            print("player2 wins")
        else:
            print("game draw")
        return

    def play(self):
        while True:
            # self.displayScores()
            print(f"Its Player {self.turn} turn")
            val = int(input("Enter 1 to pick, 2 to skip\n"))
            if(val == 2):
                if self.isLastSkipped==True:
                    self.endGame()
                    return
                self.isLastSkipped =True
                if self.turn==1:
                    self.turn=2
                else:
                    self.turn=1
                self.displayScores()
                continue

            index = random.randint(0,len(self.deck.cards)-1)
            card = self.drawCard(index)
            val = card.value
            if self.turn == 1:
                if val == 1 and self.player1.points>=11:
                    self.player1.points+=1
                elif val == 1 and self.player1.points<11:
                    self.player1.points+=11
                else:
                    self.player1.points+=val
                
                if self.player1.points==21:
                    self.endGame()
                elif self.player1.points>21:
                    print("player2 wins")
                    return
                else:
                    self.turn = 2

                self.displayScores()
                continue

            if self.turn == 2:
                if val == 1 and self.player2.points>=11:
                    self.player1.points+=1
                elif val == 1 and self.player2.points<11:
                    self.player2.points+=11
                else:
                    self.player2.points+=val
                
                if self.player2.points==21:
                    print("player2 wins")
                    return
                elif self.player2.points>21:
                    print("player1 wins")
                    return
                else:
                    self.turn =1
                self.displayScores()
            

    def drawCard(self, index):
        card = self.deck.cards[index]
        self.deck.cards.remove(self.deck.cards[index])
        print(f"You have drawn {card.value}\n")
        return card

game = Game("merwin", "samuel")
game.play()