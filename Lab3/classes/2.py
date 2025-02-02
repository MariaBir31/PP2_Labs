class  shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length*self.length


shape = shape()
print("Shape area:", shape.area()) 

square = Square(5)
print("Square area:", square.area())  