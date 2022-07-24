from glob import glob
from unittest import result
from player import Player
from board import Board

game = None

class Game():
    def __init__(self, player1name, player2name):
        self.player1 = Player(player1name,"O")
        self.player2 = Player(player2name,"X")
        self.board = Board()
        self.turn = 1

    @staticmethod
    def createGame(player1name, player2name):
        global game
        if game!=None:
            return game
        game = Game(player1name, player2name)
        return game
    

    def play(self, cellIndex):
        if cellIndex>9 or cellIndex<1:
            return "Wrong Cell Number"

        cellIndex-=1

        if self.turn == 1:
            isMarked, message = self.player1.markCell(self.board.cells[cellIndex])
            if not isMarked:
                return message
            self.activePlayer = 2
        else:
            isMarked, message = self.player2.markCell(self.board.cells[cellIndex])
            if not isMarked:
                return message
            self.activePlayer = 1

        result_symbol = self.board.resultAnalyser()
        if result_symbol=="":
            return
        if self.player1.symbol == result_symbol:
            print(f"{self.player1.name} Won")
        else:
            print(f"{self.player2.name} Won")


newGame = Game.createGame("meriwn", "samuel")