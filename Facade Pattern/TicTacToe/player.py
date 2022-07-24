from cell import Cell

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def markCell(self, cell):
        if cell.isMarked():
            return False, "Already Marked"
        if self.symbol=="X" or self.symbol=="O":
            cell.mark = self.symbol
        else:
            cell.mark = ""
        
        return True, "Cell Marked"