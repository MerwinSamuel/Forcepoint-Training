class Cell():
    def __init__(self, mark = ""):
        self.mark = mark
    
    def isMarked(self):
        if self.mark=="X" or self.mark =="O":
            return True
        return False