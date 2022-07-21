import uuid
class Seat:
    allSeats = []
    def __init__(self, seatNo, passenger_id=None, isBooked=False):
        self.seatId = uuid.uuid4()
        self.seatNo = seatNo
        self.passenger_id = passenger_id
        self.isBooked = isBooked
        # self.seatType = seatType

    @staticmethod
    def addSeat(seatNo,passenger_id,isBooked):
        seat = Seat(seatNo, passenger_id, isBooked)
        Seat.allSeats.append(seat)
        return seat

    @staticmethod
    def findById(seatId):
        for i in Seat.allSeats:
            if i.seatId == seatId:
                return seatId


    def isBooked(self):
        return self.isBooked()

    def deleteSeat(self,seatNo):
        for i in Seat.allSeats:
            if self.seatNo == seatNo:
                i.isBooked =False

