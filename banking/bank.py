class Bank: 
    bankId = -1
    allBanks = []
    def __init__(self, fullName, bankAbbrv):
        self.fullName = fullName
        self.bankAbbrv = bankAbbrv
        Bank.bankId += 1
        self.bankId = Bank.bankId

    @staticmethod
    def findBank(bankAbbrv):
        for i in Bank.allBanks:
            if i.bankAbbrv == bankAbbrv:
                return True,i
        return False, None

    @staticmethod
    def createNewBank(fullName, bankAbbrv):
       
        isBankExist, bankObject = Bank.findBank(bankAbbrv)
        if not isBankExist:
            return False, "Bank bankAbbrv alrady exist"
        if bankObject.fullName == fullName:
            return False, "Bank full name alrady exist"

        newBank = Bank(fullName, bankAbbrv)
        Bank.allBanks.append(newBank)
        return True, "Bank Created!"