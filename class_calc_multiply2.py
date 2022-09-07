class Calcu_mul:
    def Mul( self, a, b ):
        c = a * b
        return c

    def add_three ( self, d, e, f ):
        g =  d + e + f
        return g



x = Calcu_mul()
result = x.Mul(2,6)
print( result )


result = x.add_three(2,6,7)
print( result )
