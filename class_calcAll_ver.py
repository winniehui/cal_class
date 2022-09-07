class CalcuAll:
    def Add( self, a1, b1 ):
        self.a1 = a1
        self.b1 = b1
        c1 = self.a1 + self.b1
        return c1

    def Mul( self, a2, b2 ):
        self.a2 = a2
        self.b2 = b2
        c2 = self.a2 * self.b2
        return c2

    def Div( self, a3, b3 ):
        self.a3 = a3
        self.b3 = b3
        c3 = self.a3 / self.b3
        return c3

    def Sub( self, a4, b4 ):
        self.a4 = a4
        self.b4 = b4
        c4 = self.a4 - self.b4
        return c4

x = CalcuAll()
ret_1 = x.Sub( 98, 12 )
print( "ret_1: ", ret_1 )

ret_2 = x.Add( 12, 73 )
print( "ret_2:  ", ret_2 )

ret_3 = x.Div( 3, 122 )
print("ret_3: ", ret_3 )

ret_4 = x.Mul( 76, 31 )
print( "ret_4: ", ret_4 )
