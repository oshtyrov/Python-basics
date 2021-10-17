class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print(f'Запуск отрисовки ручки {self.title}.')


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print(f'Запуск отрисовки карандаша {self.title}.')


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print(f'Запуск отрисовки маркера {self.title}.')


handle_1 = Handle('Parker')
handle_1.draw()
pencil_1 = Pencil('Barker')
pencil_1.draw()
pen_1 = Pen('Jarker')
pen_1.draw()


