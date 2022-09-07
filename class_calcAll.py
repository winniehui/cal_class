class CalcuAll:
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

x = CalcuAll( 33, 61 )
result_1 = x.Sub()
print( "result_1: ", result_1 )

x2 = CalcuAll( 12, 73 )
result_2 = x2.Add()
print( "result_2:  ", result_2 )

x3 = CalcuAll( 3, 122 )
result_3 = x3.Div()
print("result_3: ", result_3 )

x4 = CalcuAll( 55, 94 )
result_4 = x4.Mul()
print( "result_4: ", result_4 )

print( "\n" )
y1 = CalcuAll( 313, 61 )
ret_1 = y1.Sub()
ret_2 = y1.Add()
ret_3 = y1.Div()
ret_4 = y1.Mul()
print( "ret_1: ", ret_1 )
print( "ret_2: ", ret_2 )
print( "ret_3: ", ret_3 )
print( "ret_4: ", ret_4 )
