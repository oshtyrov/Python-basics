class Car:
    def __init__(self, name, speed, color=None):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Автомобиль {self.name} тронулся.')

    def stop(self):
        print(f'Автомобиль {self.name} остановился.')

    def turn_right(self):
        print(f'Автомобилт {self.name} повернул направо.')

    def turn_left(self):
        print(f'Автомобиль {self.name} повернул налево.')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} равна {self.speed} км/ч.')


class TownCar(Car):
    def __init__(self, name, speed, color=None):
        super(TownCar, self).__init__(name, speed, color)

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание, скорость автомобиля {self.name} свыше 60 км/ч!({self.speed} км/ч)')
        else:
            super(TownCar, self).show_speed()


class SportCar(Car):
    def __init__(self, name, speed, color=None):
        super(SportCar, self).__init__(name, speed, color)


class WorkCar(Car):
    def __init__(self, name, speed, color=None):
        super(WorkCar, self).__init__(name, speed, color)

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание, скорость автомобиля {self.name} свыше 40 км/ч!({self.speed} км/ч)')
        else:
            super(WorkCar, self).show_speed()


class PoliceCar(Car):
    def __init__(self, name, speed, color=None):
        super(PoliceCar, self).__init__(name, speed, color)


work_kar_1 = WorkCar('Матильда', 40)
work_kar_1.go()
work_kar_1.turn_left()
work_kar_1.turn_right()
work_kar_1.show_speed()
work_kar_1 = WorkCar('Матильда', 65)
work_kar_1.show_speed()
work_kar_1.stop()
