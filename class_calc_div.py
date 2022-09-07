class Calcu_div:
    def __init__( self, a, b):
        self.a = a
        self.b = b

    def Div( self ):
        c = self.a / self.b
        return c

x = Calcu_div( 33, 12 )
result = x.Div()
print( result )
