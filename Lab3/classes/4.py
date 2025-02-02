import math


class point :
    def __init__(self, x,y):
        self.x = x 
        self.y = y

    def show(self):
        print("Coordinates :", self.x, " ", self.y)

    def move(self, new_x,new_y):
        self.x = new_x
        self.y = new_y
        print(f"New coordinates {self.x} and {self.y}")

    def dist(self, x, y):
        res_x = (x-self.x)**2 
        res_y = (y-self.y)**2
        res = (res_x + res_y)**0.5
        print(f'Distance : {res}')



s1 = point(-1, 3)


s1.show()
s1.move(6,2 )
s1.show()
s1.dist(-1, 3)