# class Fraction:
#     def __init__(self,numerator,denominator):
#         self.num = numerator
#         self.denom = denominator

# fract1 = Fraction(2,7)
# fract2 = Fraction(3,8)
# print(fract1.num)
# print(fract2.num)


class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.denom = denominator
    
    def add(self,f2):
        return Fraction((self.num*f2.denom) + (self.denom*f2.num),self.denom*f2.denom)
    def __str__(self): # its a magic function so it will cal itself
        return f"{self.num}/{self.denom}"
f1 = Fraction(2,4)
f2 = Fraction(1,4)
ans = f1.add(f2)
print(ans)