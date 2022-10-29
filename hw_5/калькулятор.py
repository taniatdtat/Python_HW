import math
import numbers 

class myExeption(Exception):
    pass

class Complex_numbers:
    exp = None # не смогла придумать как без переменной класса нормально переопределить print
                          #чтобы понимать когда в какой форме (экспоненциальной или нет) печатать 

    def __init__ (self, Re, Im):
        self.set(Re,Im)

    def set (self, x, y):
        
        if isinstance (x, numbers.Number) and isinstance (y, numbers.Number):
            self.Re = x
            self.Im = y
        else:
            raise ValueError 

    def __abs__ (self):
        return round(math.sqrt ( ( self.Re **2 ) + ( self.Im**2 ) ),2)

    def get_argument (self):
        if self.Re == 0 and self.Im  > 0 :
            return round(math.pi / 2, 2)
        elif self.Re == 0 and self.Im  < 0 :
            return round( - math.pi / 2,2)
        elif self.Re > 0:
            return round(math.atan ( self.Im / self.Re ),2)
        elif self.Re <  0 and self.Im >= 0:
            return round(math.pi + math.atan ( self.Im / self.Re ),2)
        elif self.Re <  0 and self.Im < 0:
            return round( - math.pi + math.atan ( self.Im / self.Re ),2)

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
        if self.Re ==0 and self.Im == 0 :
            raise myExeption ("Не верно введены исходные данные")
        else:
            Complex_numbers.exp = True
            return Complex_numbers(abs(self) , self.get_argument())

    def from_exponential_form (self) :
        Complex_numbers.exp = False
        return Complex_numbers(round(self[0] * math.cos (self[1]),2) , round(self[0]* math.sin (self[1]),2))
    
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
             return Complex_numbers ( round((self.Re*other.Re + self.Im*other.Im)/(other.Re**2 + other.Im**2),2) ,  round((- self.Re*other.Im + self.Im*other.Re)/(other.Re**2 + other.Im**2),2))
        else:
             return Complex_numbers (self.Re / other,  self.Im /other)

# печать
    def __str__(self):
        if Complex_numbers.exp :
            return str(self[0]) + ' *exp(  '  + str(self[1])+ ' )'
        else:
            if self[1]>=0:
                return str(self[0]) + ' + '  + str(self[1])+ 'i'
            else:
                return str(self[0]) + ' - '  + str(-self[1])+ 'i'


print(" Введите первое комплексное число a+ib в виде a b, аналогично введите второе число с новой строки ")
try:
    x1, y1 = map(float,input().split())
    x2, y2 = map(float,input().split())  
    
except ValueError:
    print("Попробуйте еще раз ввести ЧИСЛА \n")

else:
        z1 = Complex_numbers(x1, y1)
        z2 = Complex_numbers(x2, y2)

print('Введите арифметическую операцию из списка: \n +   сложение \n -   вычитание \n *   умножение \n /   деление \n to_exp   перевод чисел в экспоненциальную форму \n from_exp   перевод чисел из экспоненциальной формы в алгебраическую \n abs   вычисление модуля \n arg    вычисление аргумента ')
operacia = input()
try:
    if operacia  not in ('+', '-', '*', '/','to_exp', 'from_exp','abs','arg'):
        raise TypeError
except TypeError:
    print ("Попробуйте еще раз и выберите операцию ИЗ СПИСКА \n")


if operacia == '+':
    print( z1+z2)
    
elif operacia == '-':
    print (z1 - z2)

elif operacia == '*':
    print (z1 * z2)   

elif operacia == '/':
    try:
        print (z1 / z2)
    except ZeroDivisionError:
        print( "Давайте не будем делить на ноль. Ведите другое число")
               
elif operacia == 'to_exp':
    print ('z1 = ', z1.to_exponential_form())
    print ('z2 = ', z2.to_exponential_form())

elif operacia == 'from_exp':
    print ('z1 = ', z1.from_exponential_form())
    print ('z2 = ', z2.from_exponential_form())

elif operacia == 'abs':
    print ('модуль z1 = ' , abs(z1))
    print ('модуль z2 = ' , abs(z2))

elif operacia == 'arg':
    print ('аргумент z1 = ', z1.get_argument())
    print ('аргумент z2 = ', z2.get_argument())












        

       
   
