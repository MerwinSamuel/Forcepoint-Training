import pytest
from board import Board

newBoard = Board()

def test_firstTest():
    flag = newBoard.create_board()
    assert flag == False

def test_secondTest():
    newBoard.cells[0].mark = "X"
    newBoard.cells[1].mark = "X"
    newBoard.cells[2].mark = "X"
    newBoard.cells[3].mark = "O"
    newBoard.cells[4].mark = "X"
    newBoard.cells[5].mark = "O"
    newBoard.cells[6].mark = "O"
    newBoard.cells[7].mark = "X"
    newBoard.cells[8].mark = "X"


    assert newBoard.resultAnalyser() == "X"

def testDrawWithEmpty():
    flag = newBoard.resultAnalyzer()
    assert flag == True

