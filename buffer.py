class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.b = []
        self.sum = 0

    def add(self, *a):
        # добавить следующую часть последовательности
        self.b += a
        while len(self.b) >= 5:
            if len(self.b) >= 5:
                for j in range(5):
                    self.sum += int(self.b[j])
                print(self.sum)
                self.sum = 0
                for j in range(5):
                    del self.b[0]


    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        return self.b

Buffer
buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]

