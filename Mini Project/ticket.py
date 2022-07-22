from hashlib import new
import imp
import uuid
import datetime
from seat import Seat

from transaction import Transaction
class Ticket:

    allTickets = []
    def __init__(self, bookingDate, bookingUserName, passengers, seats, trainNo, transactionId, totalAmount):
        self.pnr_no = uuid.uuid4()
        self.bookingDate = bookingDate
        self.bookingUserName = bookingUserName
        self.passengers = passengers
        self.seats= seats
        self.transactionId = transactionId
        self.trainNo =trainNo
        self.totalAmount = totalAmount


    @staticmethod
    def bookTicket(trainNo, date, passengers, seats, bookingUserName, totalCost):
        # print(totalCost)
        # newBookTicket = Ticket.bookTicket(trainNo, passengers, seats, bookingUserName)
        

        bookSeats=[]
        # for i in BookingInterface.allBookingInterface:
        #     if i.trainNo ==trainNo and i.date == date:
        #         bookingInterfaceObj = i

        for i in seats:
            if i.isBooked == False:
                i.isBooked = True
                bookSeats.append(i)
                # bookingInterfaceObj.totalSeats -= 1
        
        newTicket = Ticket(datetime.date.today(), bookingUserName, passengers, bookSeats,trainNo, None, totalCost)

        Ticket.allTickets.append(newTicket)

        transaction = Transaction.createTransaction(newTicket.pnr_no,bookingUserName,totalCost, datetime.date.today())

        newTicket.transactionId = transaction.id

        print(newTicket)
        
        return newTicket

    def viewTicket(self):
        print(f"PNR No: {self.pnr_no}")
        print(f"Train No: {self.trainNo}")
        print(f"Booking Date: {self.bookingDate}")
        print(f"Booking User Name: {self.bookingUserName}")
        for i in range(0, len(self.passengers)):
            print(f"{self.passengers[i].passengerName} {self.passengers[i].passengerAge} {self.passengers[i].passengerGender} {self.seats[i].seatNo} ")
        print(f"Transaction Id: {self.transactionId}")

    
    @staticmethod
    def deleteTicket(pnr_no):
        allTickets = Ticket.allTickets
        for i in allTickets:
            if i.pnr_no == pnr_no:
                Ticket.allTickets.remove(i)
                return
        print("PNR No does not exist")
