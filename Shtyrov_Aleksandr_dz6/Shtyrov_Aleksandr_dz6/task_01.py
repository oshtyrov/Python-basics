from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        colors = [['red', 7], ['yellow', 2], ['green', 7]]
        while True:
            for color, sec in colors:
                self.__color = color
                print(f'Color is {self.__color}, wait {sec} seconds.')
                sleep(sec)


a = TrafficLight()
a.running()
