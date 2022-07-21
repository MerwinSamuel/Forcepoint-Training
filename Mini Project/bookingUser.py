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

    
    def bookTrainByNo(self, trainNo, date, passengerList, userName):
        bookingInterfaceList = BookingInterface.allBookingInterface
        for i in bookingInterfaceList:
            if i.trainNo == trainNo and i.date ==date:
                if i.totalSeats >= len(passengerList):
                    train = Train.findTrainByNo(trainNo)
                    perTicketCost = train.costPerTicket
                    totalCost = perTicketCost*len(passengerList)
                    # user = BookingUser.findById(userName)
                    wallet = Wallet.findByUserName(userName)
                    if not wallet.totalAmount>=totalCost:
                        print("Can't book tickets, wallet balance is low")
                        return
                    ticket = Ticket.bookTicket(trainNo, date, passengerList, i.seats, userName)
                    print("\nYour Ticket has been Successfully Booked!")
                    ticket.viewTicket()
                else:
                    print("Seat not available")
    
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





