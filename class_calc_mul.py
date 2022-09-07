class Calcu_mul:
    def __init__( self, a, b):
        self.a = a
        self.b = b

    def Mul( self ):
        c = self.a * self.b
        return c

x = Calcu_mul( 33, 12 )
result = x.Mul()
print( result )
