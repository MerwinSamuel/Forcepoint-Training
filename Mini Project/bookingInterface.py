# from train import Train
# class BookInterface:
#     allTrainsDict = {}
#     def __init__(self,source,destination,date):
#         self.source = source
#         self.destination = destination
#         self.date = date
#     def findTrainByDate(self,date):
#         print("amit")
#         for i in Train.allTrains:
#             print(BookInterface.allTrainsDict[date])
#             if not date in BookInterface.allTrainsDict.keys():
#                 BookInterface.allTrainsDict[date]=[i]
#             else:
#                 BookInterface.allTrainsDict[date].append(i)

#             print(i.sleeperSeats)
#         print(BookInterface.allTrainsDict)

class BookingInterface:
    allBookingInterface = []
    def __init__(self, date, trainNo, seats,totalSeats):
        self.date = date
        self.trainNo = trainNo
        self.seats = seats
        self.totalSeats = totalSeats

    @staticmethod
    def createBookingInterface(date, trainNo, seats, totalSeats):
        bookingInterfaceObj = BookingInterface(date, trainNo, seats, totalSeats)
        BookingInterface.allBookingInterface.append(bookingInterfaceObj)

        

    