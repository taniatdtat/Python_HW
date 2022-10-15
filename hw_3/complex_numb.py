import math
class complex_numbers:

    def __init__ (self, Re, Im):
        self.Re = Re
        self.Im = Im

    def get_module (self):
        return math.sqrt ( ( self.Re **2 ) + ( self.Im**2 ) )

    def get_argument (self):
        if self.Re == 0 and self.Im  > 0 :
            return math.pi / 2
        elif self.Re == 0 and self.Im  < 0 :
            return  - math.pi / 2
        elif self.Re > 0:
            return math.atan ( self.Im / self.Re )
        elif self.Re <  0 and self.Im >= 0:
            return math.pi + math.atan ( self.Im / self.Re )
        elif self.Re <  0 and self.Im < 0:
            return  - math.pi + math.atan ( self.Im / self.Re )

    def get_complex_num (self):                   # Получение самого числа в виде Re(x) + i Im(x)
        return  complex (self.Re, self.Im)
    
    def get_conjugate_num (self):                 # Получение сопряженного числа  Re(x) - i Im(x)
        return complex (self.Re, - self.Im)
        
    def set (self, x, y):   
        self.Re = x
        self.Im = y
        
 # Экспоненциальная форма, или туда и обратно :)
 
    def to_exponential_form (self) :        
        return self.get_module() , self.get_argument()

    def from_exponential_form (self) :
        return complex (self.get_module() * math.cos (self.get_argument()) , self.get_module() * math.sin (self.argument()))
    
# сложение, вычитание, умножение, деление

    def __add__(self, other):
        return complex( self.Re + other.Re, self.Im + other.Im)
    
    def __sub__(self, other):
        return complex( self.Re - other.Re, self.Im - other.Im)
    
    def __mul__(self, other):
        return complex( self.Re*other.Re - self.Im*other.Im,  self.Re*other.Im + self.Im*other.Re)
    
    def __truediv__(self, other):
        return complex((self.Re*other.Re + self.Im*other.Im)/(other.Re**2 + other.Im**2) ,  (- self.Re*other.Im + self.Im*other.Re)/(other.Re**2 + other.Im**2))
    




"""
z1 = complex_numbers (1, 1)
z2 = complex_numbers (3, 4)


print(z1.__add__(z2))
print(z1.__sub__(z2))
print(z1.__mul__(z2))
print(z1.__truediv__(z2))
print ('module = ' , z2.get_module())
print ('arg = ', z1.get_argument())

#print(z1.get_complex_num())
#print (z1.get_conjugate_num())

print (z2.to_exponential_form ())
print(z1.from_exponential_form )
"""







        

       
   
