class Calcu:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def Add(self):
        c = self.a + self.b
        return c


x = Calcu(29, 13)
result = x.Add()
# print("result: ", result)
# print(x.a)
# print(x.b)

y = Calcu(33, 22)
print(y.a)
print(y.b)
