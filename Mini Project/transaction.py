import uuid


class Transaction:
    allTransaction=[]
    def __init__(self, train_pnr_no, userName, totalAmount,date) -> None:
        self.id = uuid.uuid4()
        self.train_pnr_no = train_pnr_no
        self.userName= userName
        self.totalAmount = totalAmount
        self.date = date
        

    @staticmethod
    def createTransaction(train_pnr_no, userName, totalAmount, date):
        transaction = Transaction(train_pnr_no, userName, totalAmount, date)
        Transaction.allTransaction.append(transaction)
        return transaction

    def viewTransaction(self):
        print(self.train_pnr_no, self.userName, self.totalAmount, self.date)