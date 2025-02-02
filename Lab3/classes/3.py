class shape:
    def __init__(self):
        pass  

    def area(self):
        return 0 


class Rectangle(shape):
    def __init__(self, length, width):
        super().__init__() 
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 


rectangle = Rectangle(5, 10)
print("Rectangle area:", rectangle.area())