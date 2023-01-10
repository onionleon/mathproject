from django.db import models
import math

# Create your models here.


class LDET(models.Model):
    
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    

    # get_gcd(self) takes the a, b, and c values of the object of the class LDET
    # and produces a list of three integer, x1, y1, and r1, where r1 is the gcd of 
    # self.a and self.b

    def get_gcd(self):
        if self.a > self.b:
            x1, x2, y1, y2 = 1, 0, 0, 1
            r1, r2 = self.a, self.b 
        elif self.a < self.b:
            x1, x2, y1, y2 = 0, 1, 1, 0 
            r1, r2 = self.b, self.a 
        
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
    
    def get_string_answer(self):
        answer_list = self.get_xy()
        string_answer = f"{self.a}*{answer_list[0]} + {self.b}*{answer_list[1]} = {self.c}" 
        return string_answer


# The class PrimeFactorization consumes a single integer, and outputs a list of all 
# prime factors of that numbers
class PrimeFactorization(models.Model):
    
    num = models.IntegerField() 

    # the function get_pf(self) takes in the number self.num and produces a list of 
    # all of the prime factors of the number self.num
    def get_pf(self):
        n = self.num
        if self.num == 1:
            return [1]
        else: 
            elst = []
            while n % 2 == 0:
                elst.append(2)
                n = n / 2
    
            for i in range(3, int(math.sqrt(n)+ 1), 2):
        
                while (n % i == 0):
                    elst.append(int(i))
                    n = n / i
    
            if n > 2:
                elst.append(int(n))

            return elst
    
    # helper_gsa(self, lst, num) takes in a list o integer, which is the prime 
    # factorization of a number and a number, and counts the number of occurrences
    # of the given number in the given list 
    def helper_gsa(self, lst, num):
        counter = 0
        for i in lst:
            if i == num:
                counter += 1
        return counter

    # get_string_answer(self) consumes a list of all factors of self.num by calling 
    # the function get_pf(), and gives the answer in a string
    # for example, get_pf(24) would produce [2, 2, 2, 3] and get_string_answer(24)
    # would produce 2^3 3 
    def get_string_answer(self):
        counter = 0
        result = ""
        elst = []
        answer = self.get_pf()
        for i in answer:
            if i not in elst:
                elst.append(i)
        for i in range(len(elst)):
            if self.helper_gsa(answer, elst[i]) == 1:
                result += f"{elst[i]} "
            else: 
                result += f"{elst[i]}^{self.helper_gsa(answer, elst[i])} "
        
        return result

# The class GCD takes in two numbers a and b it contains the function get gcd, that 
# takes in the two numbers a and b and returns its greatest common divisor 
class Gcd(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()

    # get_gcd(self) uses the numbers a and b and returns the greatest common divisor 
    # of the numbers a and b
    def get_gcd(self):
        if self.a > self.b:
            x1, x2, y1, y2 = 1, 0, 0, 1
            r1, r2 = self.a, self.b 
        elif self.a < self.b:
            x1, x2, y1, y2 = 0, 1, 1, 0 
            r1, r2 = self.b, self.a 
        
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
                return r1

class CRT(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    m = models.IntegerField()
    #a2 = models.IntegerField()
    #b2 = models.IntegerField()
    #m2 = models.IntegerField()

    def getCRT(self):
        return self.a

    def get_string_answer(self):
        result = "poopootest"
        return result