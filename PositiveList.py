class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
            return 'ok'
        else:
            raise NonPositiveError(str(x) + ' is not positive')
PositiveList
a = PositiveList()
print(a.append(0))
