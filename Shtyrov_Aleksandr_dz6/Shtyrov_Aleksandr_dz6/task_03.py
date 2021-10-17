class Worker:
    def __init__(self, name, surname, wage, bonus, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus, position=None):
        super().__init__(name, surname, wage, bonus, position)

    def get_full_name(self):
        print(f'Полное имя должностного лица: {self.name} {self.surname}.')

    def get_total_income(self):
        print(f'Доход {self.name} {self.surname} с '
              f'учетом премии: {sum(self._income.values())} руб.')


position_1 = Position('Иннокентий', 'Иннокентьев', 1000, 200)
position_1.get_full_name()
position_1.get_total_income()
