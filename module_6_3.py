class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        # Инициализируем Horse
        super().__init__()
        # Инициализируем Eagle
        Eagle.__init__(self)

    def move(self, dx, dy):
        # Используем методы родителей через super()
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        # Печатаем звук, унаследованный от Eagle
        print(self.sound)

# Проверка работы
p1 = Pegasus()
print(p1.get_pos())  # Ожидаемый вывод: (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # Ожидаемый вывод: (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # Ожидаемый вывод: (5, 35)
p1.voice()  # Ожидаемый вывод: I train, eat, sleep, and repeat