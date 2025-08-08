class Fraction:
    
    def __init__(self,x,y):
        self.num = x
        self.den = y
        
    def __str__(self):
        return f'{self.num}/{self.den}'
    
    def __add__(self,other):
        new_num = (self.num*other.den) + (other.num*self.den)
        new_den = self.den*other.den
        return f'{new_num}/{new_den}'
    
    def __sub__(self,other):
        new_num = (self.num*other.den) - (other.num*self.den)
        new_den = self.den*other.den
        return f'{new_num}/{new_den}'
    
    def __mul__(self,other):
        new_num = (self.num*other.num) 
        new_den = (other.den*self.den)
        return f'{new_num}/{new_den}'
    
    def __truediv__(self,other):
        new_num = (self.num*other.den) 
        new_den = (other.num*self.den)
        return f'{new_num}/{new_den}'
    
    def convert_to_decimal(self):
        return self.num/self.den