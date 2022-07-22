from bookingInterface import BookingInterface
from train import Train
from station import Station
from trainRoute import TrainRoute
from seat import Seat
from bookingUser import BookingUser

class Admin:
    def __init__(self,adminUsername,adminPassword) -> None:
        self.adminUsername = adminUsername
        self.adminPassword = adminPassword

    def addTrain(self, trainNo, trainName, trainRouteId, costPerTicket, totalSeats):
        newtrain = Train.addNewTrain(trainNo, trainName, trainRouteId, costPerTicket, totalSeats)
        return newtrain

    def updateTrain(userName,newproerty,newValue):
        pass
        # setattr(objectTrain,newproerty,newValue)

    def addStation(self,stationName, stationState, stationPinCode):
        newStation = Station.createStation(stationName, stationState, stationPinCode)
        return newStation

    def deleteStation():
        pass

    def addSeat(self,seatNo,passenger_id,isBooked):
        newSeat = Seat.addSeat(seatNo,passenger_id,isBooked)
        return newSeat

    def addTrainRoute(self,trainNo,listOfStation):
        newTrainRoute = TrainRoute.createTrainRoute(trainNo,listOfStation)
        return newTrainRoute

    def updatestation(userName,newproerty,newValue):
        pass
   
    def createBookingInterface(self, date, train, seats, totalSeats):
        BookingInterface.createBookingInterface(date, train, seats, totalSeats)
    
    def createBookingUser(self, userName, password ):
        newBookingUser =  BookingUser.createBookingUser(userName,password)
        return newBookingUser
    
    def viewAllTrains(self):
        Train.viewAllTrains()

