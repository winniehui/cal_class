class Calcu_sub:
##    def __init__( self, a, b):
##        self.a = a
##        self.b = b

    def Sub( self,a ,b ):
        self.a = a
        self.b = b
        c = self.a - self.b
        return c

x = Calcu_sub()
result = x.Sub(3,2)
print( result )
