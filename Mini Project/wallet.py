import uuid
class Wallet:
    allWallets = []
    def __init__(self, userName, totalAmount) -> None:
        self.id = uuid.uuid4()
        self.userName = userName
        self.totalAmount = totalAmount

    @staticmethod
    def createWallet(userName, totalAmount):
        wallet = Wallet(userName, totalAmount)
        Wallet.allWallets.append(wallet)
        return wallet

    def addAmount(self, amount):
        self.totalAmount+=amount
        print(self.totalAmount)

    @staticmethod
    def findById(walledId):
        for i in Wallet.allWallets:
            if i.id == walledId:
                return i

    @staticmethod
    def findByUserName(userName):
        for i in Wallet.allWallets:
            if i.userName == userName:
                return i

    def isBalanceSufficient(self, amout):
        if self.totalAmount>=amout:
            return True
        else:
            return False

