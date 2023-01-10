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
    a1 = models.IntegerField()
    b1 = models.IntegerField()
    m1 = models.IntegerField()
    a2 = models.IntegerField()
    b2 = models.IntegerField()
    m2 = models.IntegerField()

    
    def get_string_answer(self):
        result = self.a1 + self.a2 + self.b1 + self.b2 + self.m1 + self.m2
        a1 = self.a1
        b1 = self.b1
        m1 = self.m1
        a2 = self.a2
        b2 = self.b2
        m2 = self.m2

        def get_gcd(beforepf_in):
            a = beforepf_in[0]
            b = beforepf_in[1]
            if a > b:
                x1, x2, y1, y2 = 1, 0, 0, 1
                r1, r2 = a, b 
            elif a < b:
                x1, x2, y1, y2 = 0, 1, 1, 0 
                r1, r2 = b, a 
            
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
        
        def get_xy(beforepf_in):
            abc = get_gcd(beforepf_in)
            #print(f"gcd check: {abc}")
            a1 = abc[0]
            b1 = abc[1]
        #     c1 = abc[2]
        #     if (beforepf[2]/c1)%1 == 0.0:
        #         factor = beforepf[2] / c1
            return [a1, b1] #has been tabbed ****************
                
        #     elif type(beforepf[2]/c1) == float:
        #         factor = beforepf[2] / c1
        #         
        #         return [int(a1 * factor), int(b1 * factor)]
        #     else:
        #         return None
        #

        if a1 != 1:
            ldetCoef = (get_xy([a1, m1, 1])[0])
            preppedEQ1 = [(a1* ldetCoef)%m1, (b1*ldetCoef)%m1, m1]
            
        if a1 == 1:
            preppedEQ1 = [a1, b1, m1]
            
            
        beforepf = [(a2*preppedEQ1[2]), (b2 - (a2*preppedEQ1[1])), m2]
        mod = beforepf[2]
        if beforepf[0] != 1:
            #ldet FN being ldet first number, which is the coefficient on the first value,
            #since the second value is useless, since it's the mod
            ldetCoef = (get_xy([beforepf[0], mod, 1])[0])
            afterpf = [(beforepf[0]* ldetCoef)%mod, (beforepf[1]*ldetCoef)%mod, mod]
            print(f"so now we have: {afterpf[0]}k = {afterpf[1]} (mod {mod})")
        #i don't think case occurs much but i do think that it will happen sometimes
        #just modding here to make numbers nicer
        else:
            afterpf = [(a2*preppedEQ1[2])%mod, (b2 - (a2*preppedEQ1[1]))%mod, mod]
            
        #first value is N(subscript 0), and second answer is simply just m1*m2, by CRT
        finalAnswer = [(preppedEQ1[1] + (preppedEQ1[2]*afterpf[1])), (preppedEQ1[2]*mod)]
        return f"x = {finalAnswer[0]} (mod {finalAnswer[1]})"