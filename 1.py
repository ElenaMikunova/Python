import time


class TrafficLight:

    __colour = ["red", "yellow", "green"]

    def running(self):
        count = 0
        while count < 2:
            print(TrafficLight.__colour[0])
            time.sleep(7)
            print(TrafficLight.__colour[1])
            time.sleep(2)
            print(TrafficLight.__colour[2])
            time.sleep(5)
            print(TrafficLight.__colour[1])
            time.sleep(2)
            count += 1
        else:
            print("Светофор выключен")


Light_1 = TrafficLight()
Light_1.running()
