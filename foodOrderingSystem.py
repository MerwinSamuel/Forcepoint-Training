from queue import Queue
from threading import Thread, current_thread
from time import sleep

class FoodOrderingSystem:
    def __init__(self, orders):
        self.orders = orders
        self.q = Queue()

    def placeOrder(self):
        for order in self.orders:
            self.q.enque(order)
            print(current_thread().name +"-"+ order)
            sleep(0.5)

    def serveOrder(self):
        while not self.q.isEmpty():
            print(current_thread().name +"-"+ self.q.deque())
            sleep(2)

if __name__ == '__main__':
    orders = FoodOrderingSystem(['pizza','samosa','pasta','biryani','burger'])
    t1 = Thread(target = orders.placeOrder)
    t2 = Thread(target = orders.serveOrder)
    t1.start()
    sleep(1)
    t2.start()