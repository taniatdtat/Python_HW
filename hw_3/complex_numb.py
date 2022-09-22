import math
class complex_numbers:

    def __init__ (self, Re, Im):
        self.Re = Re
        self.Im = Im


    def get_module (self):
        return math.sqrt ( ( self.Re **2 ) * ( self.Im**2 ) )

    
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

        
    def det_complex_num (self):                   # Получение самого числа в виде Re(x) + i Im(x)
        return complex(self.Re, self.Im)
    
    def get_conjugate_num (self):                 # Получение сопряженного числа  Re(x) - i Im(x)
        return complex(self.Re, - self.Im)
        
    def set_Re (self, x):   # Изменение действительной части
        self.Re = x
        
    def set_Im (self, x):   # Изменение мнимой части 
        self.Im = x
      
    def to_exponential_form (self) :        # Экспоненциальная форма, или туда и обратно :)
        return ( str(self.det_module()) + 'exp' + '(' +  str(self.argument) + ')')   

    def from_exponential_form (self) :
        return complex (self.module() * math.cos (self.argument()) , self.module() * math.sin (self.argument())) 


z1 = complex_numbers (1, 1)
z2 = complex_numbers (3, 4)

print ('module = ' , z2.get_module())    
print (z1.get_complex_num)
print (z1.get_conjugate_num())
print ('module = ' , z2.get_module())





        

       
   
