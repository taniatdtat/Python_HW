class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"

def dist(a, b):
    return  ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5


class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type) +" \n"+ "area =  " + str(self.area()) +"\n"+ "perimeter = " +str(self.perimeter())
    

class Polygon (Shape):
    def __init__(self, *args, type = "Polygon"):
        self._args = args
        self._type = type

    def kol_arg(self):
        k = 0
        for arg in self._args:
            k+=1
        return k
            
    def perimeter(self):
        p = 0
        for i  in  range(self.kol_arg() -2) :
            p += dist(self._args[i], self._args[i+1])
        p +=dist(self._args[0], self._args[-2])
        return round(p,2)
    
    
class Triangle(Polygon):
    def __init__(self, p1, p2, p3, type="Triangle"):
        super().__init__(p1, p2, p3, type = type)
        

        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3


        self._a = dist (self._point_1, self._point_2)
        self._b = dist (self._point_2, self._point_3)
        self._c = dist (self._point_1, self._point_3)

    def area(self):
        pp = self.perimeter()/2
        return round((pp * (pp - self._a) * (pp - self._b) * (pp - self._c)) ** 0.5, 2)

class Tetragon (Polygon):
        def __init__(self, p1, p2, p3,p4, type = "Tetragon"):
            super().__init__(p1, p2, p3, p4, type = type)
            self._point_1 = p1
            self._point_2 = p2
            self._point_3 = p3
            self._point_4 = p4
       

            
class Rectangle(Tetragon):
        def __init__(self, p1, p2, p3, p4, type = "Rectangle"):
            super().__init__(p1, p2, p3, p4,type=type)
    
            self._a = dist (self._point_1, self._point_2)
            self._b = dist (self._point_2, self._point_3)
        

        def area(self):
            return  round (self._a * self._b , 2)
    

class Square (Rectangle):
    def __init__(self, p1, p2, p3, p4, type = "Square"):
        super().__init__(p1, p2, p3, p4, type = type)

            
    
class Rhombus (Tetragon ):
    def __init__(self, p1, p2, p3, p4, type = "Rhombus"):
        super().__init__(p1, p2, p3, p4, type = type)
        
        self._diag_1 = dist(self._point_1, self._point_3)
        self._diad_2 = dist(self._point_2, self._point_4)

    def area(self):
        return round(0.5 *self._diad_1 *self._diad_2  , 2)


class Circle ( Shape):
    
    def __init__(self, centre, r, type = "Circle"):
        super().__init__(type)
        
        self._centre = centre
        self._r = r

    def area(self):
        return round(3.14 *self._r ** 2, 2)

    def perimeter(self):
        return round( 2 * 3.14 *self._r, 2)


   
#a = Triangle(Point(), Point(1, 1), Point(2, 3))


#b = Circle (Point(1, 1), 3)
c = Rectangle(Point(), Point(0, 1), Point(2, 1), Point(2,0))
d = Square(Point(), Point(0, 1), Point(1, 1), Point(1,0))
print(d)
print(c)
