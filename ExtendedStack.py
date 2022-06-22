class ExtendedStack(list):
    def sum(self):
        top1 = self[len(self) - 1]
        self.pop(len(self) - 1)
        top2 = self[len(self) - 1]
        self.pop(len(self) - 1)
        self.append(top1 + top2)
        # операция сложения


    def sub(self):
        top1 = self[len(self) - 1]
        self.pop(len(self) - 1)
        top2 = self[len(self) - 1]
        self.pop(len(self) - 1)
        self.append(top1 - top2)
        # операция вычитания


    def mul(self):
        top1 = self[len(self) - 1]
        self.pop(len(self) - 1)
        top2 = self[len(self) - 1]
        self.pop(len(self) - 1)
        self.append(top1 * top2)
        # операция умножения


    def div(self):
        top1 = self[len(self) - 1]
        self.pop(len(self) - 1)
        top2 = self[len(self) - 1]
        self.pop(len(self) - 1)
        self.append(top1//top2)
        # операция целочисленного деления


ExtendedStack
x = ExtendedStack([1, 2, 3, 4, 5, 6])
x.sum()
print(x)
x.sub()
print(x)