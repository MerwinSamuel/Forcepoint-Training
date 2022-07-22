from tarfile import LENGTH_LINK
import uuid
from structlinks.DataStructures import LinkedList

class TrainRoute:
    allTrainRoutes=[]
    def __init__(self,trainNo,listOfStation):
        self.trainNo = trainNo
        self.listOfStation = listOfStation
        self.trainRouteId = uuid.uuid4()
    
    @staticmethod
    def createTrainRoute(trainNo,listOfStation):
        print(listOfStation)
        linkedList = LinkedList()

        print(linkedList)

        for i in listOfStation:
            print(i)
            # linkedList.append(i.stationId)4
            linkedList.append(i)

        # print(f"Linked List {linkedList}")

        
        trainRoute = TrainRoute(trainNo, linkedList)
        TrainRoute.allTrainRoutes.append(trainRoute)
        print(f"Train No {trainNo} route has been created")
        return trainRoute



    # def updateTrainRoute(self, propertyName, newValue):
    #     setattr(self,propertyName,newValue)
    #     return "Value updated"

    def deleteTrainRoute(self):
        for i in TrainRoute.allTrainRoutes:
            if self.trainNo == i.trainNo:
                TrainRoute.allTrainRoutes.remove(i)

    def viewTrainRoute(self):
        i = 1
        print(f"Train Route for {self.trainNo} is:")
        linkedList = self.listOfStation
        node = linkedList._first
        while node:
            station = node.item

            print(f"{i}. {station.stationName}")
            node = node.next
            i+=1


    # def delete(self, trainNo, listOfStation,):
    #     for i in listOfStation:
    #         TrainRoute.allTrainRoutes.remove(i)