import uuid
from bookingInterface import BookingInterface
from passenger import Passenger
from ticket import Ticket
from wallet import Wallet
from train import Train

class BookingUser:
    allUsers= []
    def __init__(self, userName, password, walletId=None) -> None:
        self.id = uuid.uuid4()
        self.userName = userName
        self.password = password
        self.walletId = walletId

    @staticmethod
    def findById(username):
        for i in BookingUser.allUsers:
            if i.userName == username:
                return i

    def createWallet(self, totalAmount):
        wallet = Wallet.createWallet(self.userName, totalAmount)
        self.walletId = wallet.id
        return wallet

    
    def bookTrainByNo(self, trainNo, date, passengerList):
        BookingInterface.checkSeatsAndBook(self.userName, trainNo, date, passengerList)
    
    @staticmethod
    def createPassenger(passengerName, passengeerAge, passengerGender):
        newPass = Passenger(passengerName, passengeerAge, passengerGender)
        return newPass

    @staticmethod
    def createBookingUser(userName,password):
        newBookingUser = BookingUser(userName,password)
        BookingUser.allUsers.append(newBookingUser)
        return newBookingUser

    def updateBookingUser(self, propertyName, newValue):
        setattr(self,propertyName,newValue)
        return "Value Updated"


    def viewPreviousBookedTickets(self):
        allTickets = Ticket.allTickets
        for i in allTickets:
            if i.bookingUserName == self.id:
                i.viewTicket()


    def cancelTicket(self, pnr_no):
        Ticket.deleteTicket(pnr_no)

    
    def viewTrainAvailability(self, trainNo, date):
        print("\nAvailable Trains:")
        BookingInterface.viewTrainAvailability(trainNo, date)

