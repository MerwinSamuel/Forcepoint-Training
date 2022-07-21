import uuid
class TrainRoute:
    allTrainRoutes=[]
    def __init__(self,trainNo,listOfStation):
        self.trainNo = trainNo
        self.listOfStation = listOfStation
        self.trainRouteId = uuid.uuid4()
    
    @staticmethod
    def createTrainRoute(trainNo,listOfStation):
        trainRoute = TrainRoute(trainNo, listOfStation)
        TrainRoute.allTrainRoutes.append(trainRoute)
        print(f"Train No {trainNo} route has been created")
        return trainRoute



    def updateTrain(self, propertyName, newValue):
        setattr(self,propertyName,newValue)
        return "Value updated"

    def deleteTrainRoute(self,trainNo):
        for i in TrainRoute.allTrainRoutes:
            if self.trainNo == trainNo:
                TrainRoute.allTrainRoutes.remove(i)


    def viewTrainRoute(self,trainNo,listOfStation):
        for i in listOfStation:
            print("List Of Station", i)
            print("Train Route",trainNo)

    def delete(self, trainNo, listOfStation,):
        for i in listOfStation:
            TrainRoute.allTrainRoutes.remove(i)