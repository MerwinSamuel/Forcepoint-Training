from cell import Cell
cell = Cell()


def test_isMarked1():
    assert cell.isMarked() == False

def test_isMarked2():
    cell.mark = "X"
    assert cell.isMarked() == True

def test_isMarked3():
    cell.mark = "O"
    assert cell.isMarked() == True

def test_isMarked4():
    cell.mark = "abc"
    assert cell.isMarked() == False
