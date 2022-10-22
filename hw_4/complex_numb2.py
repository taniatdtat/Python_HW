import math
class Complex_numbers:

    def __init__ (self, Re, Im):
        self.set(Re,Im)

    def set (self, x, y):   
        self.Re = x
        self.Im = y


    def __abs__ (self):
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

    def get (self):                 
        return  self.Re, self.Im

    
#доступ по ключу
    
    def __getitem__(self, key):
        if key != 0 and key != 1:
            return False
        if key == 0:
            return self.Re
        return self.Im
    

    def __setitem__(self, key, value):
        if key != 0 and key != 1:
            return False
        if key == 0:
            self.Re = value
        else:
            self.Im = value

        
 # Экспоненциальная форма
 
    def to_exponential_form (self) :        
        return abs(self) , self.get_argument()

    def from_exponential_form (self) :
        return Complex_numbers( abs(self) * math.cos (self.get_argument()) , abs(self) * math.sin (self.get_argument()))
    
# сложение, вычитание, умножение, деление

    def __add__(self, other): 
        if  isinstance(other, Complex_numbers):
            return  Complex_numbers (self.Re + other.Re, self.Im + other.Im)
        else:
            return Complex_numbers (self.Re + other,  self.Im )

     
    def __sub__(self, other):
        if  isinstance(other, Complex_numbers):
            return  Complex_numbers (self.Re - other.Re, self.Im - other.Im)
        else:
            return Complex_numbers (self.Re - other,  self.Im )

    
    def __mul__(self, other):
        if  isinstance(other, Complex_numbers):
            return  Complex_numbers (self.Re*other.Re - self.Im*other.Im,  self.Re*other.Im + self.Im*other.Re)
        else:
            return Complex_numbers (self.Re * other,  self.Im *other)
        
    
    def __truediv__(self, other):
        
        if  isinstance(other, Complex_numbers):
             return Complex_numbers ( (self.Re*other.Re + self.Im*other.Im)/(other.Re**2 + other.Im**2) ,  (- self.Re*other.Im + self.Im*other.Re)/(other.Re**2 + other.Im**2))
        else:
             return Complex_numbers (self.Re / other,  self.Im /other)
'''
# печать
    def __str__(self):
        return str(self[0]) + ' + '  + str(self[1])+ 'i'

        #return str(self.r) + ' exp(  '  + str(self.arg)+ ' )'

     '''      
z1 = Complex_numbers (2, 5)
z2 = Complex_numbers (3, 4)
'''
print(z1[0])
print(z1)
z1[0] = 11
print(z1)
print(z1+z2)
print(z1- z2)
print(z1*z2)
print(z1/z2)'''
print ('module z1 = ' , abs(z1))
print ('arg z1 = ', z1.get_argument())

print(z1.to_exponential_form)








        

       
   
