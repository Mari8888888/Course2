import datetime
s = [int(i) for i in input().split()]
a = datetime.date(s[0], s[1], s[2])
n = int(input())
b = datetime.timedelta(n)
d = a + b
print(d.year, d.month, d.day)
