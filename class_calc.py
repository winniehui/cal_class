class Calc:
    def __init__( self, a, b):
        self.a = a
        self.b = b

    def Add( self ):
        c = self.a + self.b
        return c

    def Mul( self ):
        c = self.a * self.b
        return c

    def Div( self ):
        c = self.a / self.b
        return c

    def Sub( self ):
        c = self.a - self.b
        return c



class sum_diff_calc(Calc):
    def __init__( self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y)

    def sum_diff(self):
        c = super().Add()
        d = super().Sub()
        e = c + d
        return e

m = sum_diff_calc(8,6)

n = m.sum_diff()
print (n)
p = m.Add()
print (p)
    
