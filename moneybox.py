class MoneyBox:
    def __init__(self, capacity):
      # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.size = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if (self.capacity - v) >= 0:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v) == True:
            self.size += v
            self.capacity -= v
            return self.size
        else:
            return 'копилка переполнена'
MoneyBox
x = MoneyBox(50)
y = MoneyBox(15)
x.add(10)
x.add(30)
y.add(12)
y.add(1)
print(x.capacity)
print(y.capacity)



