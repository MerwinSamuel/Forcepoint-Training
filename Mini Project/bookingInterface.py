import uuid
from train import Train
from wallet import Wallet
from ticket import Ticket

class BookingInterface:
    allBookingInterface = []
    def __init__(self, date, trainNo, seats,totalSeats):
        self.id = uuid.uuid4()
        self.date = date
        self.trainNo = trainNo
        self.seats = seats
        self.totalSeats = totalSeats

    @staticmethod
    def createBookingInterface(date, trainNo, seats, totalSeats):
        bookingInterfaceObj = BookingInterface(date, trainNo, seats, totalSeats)
        BookingInterface.allBookingInterface.append(bookingInterfaceObj)

    
    def deleteBookingInterface(self):
        for i in BookingInterface.allBookingInterface:
            if i.id == self.id:
                BookingInterface.allBookingInterface.remove(i)

    @staticmethod
    def checkSeatsAndBook(userName, trainNo, date, passengerList):
        bookingInterfaceList = BookingInterface.allBookingInterface
        for i in bookingInterfaceList:
            if i.trainNo == trainNo and i.date ==date:
                if i.totalSeats >= len(passengerList):
                    train = Train.findTrainByNo(trainNo)
                    perTicketCost = train.costPerTicket
                    totalCost = perTicketCost*len(passengerList)
                    wallet = Wallet.findByUserName(userName)
                    if wallet.isBalanceSufficient(totalCost):
                        wallet.totalAmount-=totalCost
                        i.totalSeats-=len(passengerList)
                        ticket = Ticket.bookTicket(trainNo, date, passengerList, i.seats,  userName, totalCost)
                        print("\nYour Ticket has been Successfully Booked!")
                        ticket.viewTicket()
                    else:
                        print("Can't book tickets, wallet balance is low")
                        return
                else:
                    print("Seats not available")

    @staticmethod
    def viewTrainAvailability(trainNo, date):
        bookingInterface = BookingInterface.allBookingInterface
        for i in bookingInterface:
            if i.date == date and i.trainNo==trainNo:
                print(f"Train No:{i.trainNo} Date: {i.date} Total available Seats:{i.totalSeats}")

                    
                    




    



    