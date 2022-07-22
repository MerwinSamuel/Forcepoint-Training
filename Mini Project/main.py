import imp
from multiprocessing.spawn import import_main_path
from telnetlib import SE
from admin import Admin
from bookingInterface import BookingInterface
# from bookingInterface import BookInterface
from seat import Seat
import datetime
from train import Train
from wallet import Wallet
admin = Admin("irctc", "1234")


##adding stations
mumbaicst = admin.addStation("Mumbai CST", "Maharashtra", "400087")
lonavala = admin.addStation("Lonavala", "Maharashtra", "400000")
pune = admin.addStation("Pune", "Maharashtra", "4000801")
chennai = admin.addStation("Chennai", "Tamil Nadu", "400087")

trainRoute12640 = admin.addTrainRoute(12640, [mumbaicst, lonavala, pune, chennai])
trainRoute12640.viewTrainRoute()
##trainRoute12640.listOfStation[3] = "Thane"

train12640 = admin.addTrain(12640, "Chennai Express",  trainRoute12640.trainRouteId, 1000, 100)
train12641 = admin.addTrain(12641, "Mumbai Express",  trainRoute12640.trainRouteId, 2000, 100)

print(train12640.__class__.__name__)

# for i in range(1,51):
#     seat = admin.addSeat(i,None, False, "sleeper")
#     train12640.addSleeperSeats(seat.seatId)
# for i in range(50,101):
#     admin.addSeat(i,None, False, "ac")
#     train12640.addAcSeats(seat.seatId)

# print(len(train12640.sleeperSeats))

# bi = BookInterface("mumbai","chan",datetime.date(2022, 7, 22))
# bi.findTrainByDate(datetime.date(2022, 7, 22))

# Train.viewTrainsByDate(datetime.date(2022, 7, 22))




# merwin.viewTrainsByDate(datetime.date(2022, 7, 22))4

#creating seats
seats = []
seats.append(Seat(1, None, False))
seats.append(Seat(2, None, False))
seats.append(Seat(3, None, False))

admin.createBookingInterface(datetime.date(2022, 7, 22), 12640, seats,3)

seats = []
seats.append(Seat(1, None, False))
seats.append(Seat(2, None, False))
seats.append(Seat(3, None, False))

admin.createBookingInterface(datetime.date(2022, 7, 23), 12640, seats, 3)

seats = []

seats.append(Seat(1, None, False))
seats.append(Seat(2, None, False))
seats.append(Seat(3, None, False))

admin.createBookingInterface(datetime.date(2022, 7, 24), 12640, seats,3)

# print(BookingInterface.allBookingInterface)

##admin creating bookingUser
merwin = admin.createBookingUser("merwin", "password@123")

#user creating wallet
merwin.createWallet(3000)
wallet = Wallet.findById(merwin.walletId)
print(f"Wallet Amount {wallet.totalAmount}")


##user creating passengers to add in the ticket
amit = merwin.createPassenger("Amit", 22, "Male")
jash = merwin.createPassenger("Jash", 22, "Male")
jay = merwin.createPassenger("Jay", 22, "Male")

list_of_passengers = [amit, jash, jay]

merwin.bookTrainByNo(12640, datetime.date(2022, 7, 22), list_of_passengers)


##view all trains
print("\nAll Trains Added By Admin")
admin = Train.viewAllTrains()


#check train availability with date and train-
merwin.viewTrainAvailability(12640, datetime.date(2022, 7, 22))



