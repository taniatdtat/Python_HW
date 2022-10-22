class Node:
    
    def __init__(self, value, prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    
    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())


    

class List:

    def __init__(self, collection = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0
        
        if isinstance(collection, int):
            self.append(collection)

        elif isinstance(collection, list):
            self + collection


    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value, self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        
        if i < 0 or i >= self._length:
            return False
        
        if i <= self._length / 2 :
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
            
        else:
            curr_pointer = self._finish_pointer
            for j in range(self._length - i - 1):
                curr_pointer = curr_pointer.get_prev()
                
        return curr_pointer.get_value()
    
    def pop(self,i):
        
        if i < 0 or i >= self._length:
            return False

        arr = List()
        for j in range (len(self)):
            if self[j] != self[i]:
                arr.append(self[j])
        return arr
        
    
    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def __add__(self,other):
        for i in range (len(other)):
            self.append( other[i])
        return self
    



A = List([777,333])
B = List()

for i in range(8):
    A.append(i)

for i in range(5):
    B.append(i)
    
print(A)
print(B)
print(A+B)
#print(A.pop(6))




