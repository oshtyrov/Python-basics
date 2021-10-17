class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self, weight_for_1m=25, thickness=5):
        weight_for_1m = weight_for_1m
        thickness = thickness
        result = self._length * self._width * weight_for_1m * thickness
        print(f'Масса асфальта, необходимая для покрытия дорожного полотна длинной'
              f' {self._length} метров, шириной {self._width} метров, составляет '
              f'{round((result / 1000), 2)} тонн.')


road_1 = Road(20, 5000)
road_1.calculate_weight()
road_1.calculate_weight(26, 6)

