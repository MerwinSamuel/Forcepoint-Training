from seat import Seat

import uuid
class Train:
    allTrains= []
    def __init__(self, trainNo, trainName, trainRouteId, costPerTicket, totalSeats):
        self.trainId = uuid.uuid4()
        self.trainNo = trainNo
        self.trainName = trainName
        self.trainRouteId = trainRouteId
        self.costPerTicket = costPerTicket
        self.totalSeats = totalSeats

    @staticmethod
    def addNewTrain(trainNo, trainName, trainRouteId, costPerTicket, totalSeats):
        newTrain = Train(trainNo, trainName, trainRouteId, costPerTicket, totalSeats)
        Train.allTrains.append(newTrain)
        print(f"Train Number {newTrain.trainNo} has beed Added")
        return newTrain


    @staticmethod
    def findTrainByNo(trainNo):
        for i in Train.allTrains:
            if i.trainNo == trainNo:
                return i


    def updateTrain(self, propertyName, newValue):
        setattr(self,propertyName,newValue)
        return "Value updated"

    def deleteTrain(self,trainNo):
        for i in Train.allTrains:
            if self.trainNo == trainNo:
                Train.allTrains.remove(i)


    def addSleeperSeats(self, seatId):
        seat = Seat.findById(seatId)
        self.sleeperSeats.append(seat)
    
    def addAcSeats(self, seatId):
        seat = Seat.findById(seatId)
        self.acSeats.append(seat)

    @staticmethod
    def viewTrainsByDate(date):
        listOfTrains=[]
        for i in Train.allTrains:
            if i.date == date:
                listOfTrains.append(i)
                print(f"{i.trainNo}-{i.trainName} - Available Seats-{i.remainingSeats}")
        

    
