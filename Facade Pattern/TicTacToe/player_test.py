from player import Player
from cell import Cell

def test_markCell1():
    player = Player("Merwin","X")
    cell = Cell()
    player.markCell(cell)
    assert cell.mark == "X"

def test_markCell2():
    player = Player("Samuel", "O")
    cell = Cell()
    player.markCell(cell)
    assert cell.mark == "O"


