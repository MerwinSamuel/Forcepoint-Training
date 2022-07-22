import uuid
from structlinks import LinkedList
class Station:
    allStations = []
    def __init__(self, stationName, stationState, stationPinCode):
        self.stationId = uuid.uuid4()
        self.stationName = stationName
        self.stationState = stationState
        self.stationPiCode = stationPinCode

    
    @staticmethod
    def createStation(stationName, stationState, stationPinCode):
        newStation = Station(stationName, stationState, stationPinCode)
        Station.allStations.append(newStation)
        print(f"Station {newStation.stationName} has been Created!")
        return newStation
        
    def updateStation(self,propertyName, newValue):
        setattr(self,propertyName,newValue)
        return "Station updated"

    def deleteStation(self,stationName):
        for i in Station.allStations:
            if self.stationName == stationName:
                Station.allStations.remove(i)