from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name
        self.total_cloth = None
        self.sum_total_cloth = None

    @property
    def get_total_cloth(self):
        if self.total_cloth is None:
            self.calc_total_cloth()
        return self.total_cloth

    @abstractmethod
    def calc_total_cloth(self):
        pass

    def __add__(self, other):
        self.sum_total_cloth = self.total_cloth + other.total_cloth
        return Clothes(self.sum_total_cloth)


class Coat(Clothes):
    def __init__(self, name, v):
        self._v = int(v)
        super().__init__(name)

    def calc_total_cloth(self):
        self.total_cloth = self._v / 6.5 + 0.5


class Suite(Clothes):
    def __init__(self, name, h):
        self._h = int(h)
        super().__init__(name)

    def calc_total_cloth(self):
        self.total_cloth = 2 * self._h + 0.3


a = Suite('Black suite', 50)
a_total_cloth = a.get_total_cloth
print(a_total_cloth)
b = Coat('Yellow Coat', 100)
b_total_cloth = b.get_total_cloth
print(b_total_cloth)
c = Coat('Black', 100)
c_total_cloth = c.get_total_cloth
print(c_total_cloth)
d = a_total_cloth + b_total_cloth + c_total_cloth
print(d)
