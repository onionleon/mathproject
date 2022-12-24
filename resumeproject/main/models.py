from django.db import models

# Create your models here.


class LDET:
    
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b 
        self.c = c
    

    # get_gcd(self) takes the a, b, and c values of the object of the class LDET
    # and produces a list of three integer, x1, y1, and r1, where r1 is the gcd of 
    # self.a and self.b

    def get_gcd(self):
        if self.a > self.b:
            x1 = 1
            x2 = 0
            y1 = 0
            y2 = 1 
            r1 = self.a 
            r2 = self.b
        elif self.a < self.b:
            x1 = 0
            x2 = 1
            y1 = 1
            y2 = 0 
            r1 = self.b
            r2 = self.a 
        
        while r2 != 0:
            q = r1//r2 
            x3 = x1 - q * x2
            y3 = y1 - q * y2
            r3 = r1 - q * r2
            x1 = x2 
            y1 = y2 
            r1 = r2 
            x2 = x3 
            y2 = y3 
            r2 = r3
            if r2 == 0:
                return [x1, y1, r1]

    # get_xy(self) produces, a list of two integers, such that the first element of 
    # of the produced list multiplied by self.a added to the second element multiplied 
    # by self.b is equal to self.c

    def get_xy(self):
        abc = self.get_gcd()
        a1 = abc[0]
        b1 = abc[1]
        c1 = abc[2]
        if type(self.c/c1) == int:
            factor = self.c / c1
            return [self.a * factor, self.b * factor, self.c * factor]
        elif type(self.c/c1) == float:
            factor = self.c / c1
            return [int(a1 * factor), int(b1 * factor)]
        else:
            return None 