class Point:
    # What is self
    # Self in a class is a variable that holds the object instance.
    # Self here would be described as Point.
    # __init__ is a special method for classes.
    def __init__(self, x, y):
        # print("Hey I am __init__")  # Whenever we create an object instance __init__ will execute.
        self.x = x  # Another way to say this is point.x = x.
        self.y = y  # Or you could say point.y = y.

    def distance(self):
        return self.x + self.y

    # Ordinary methods will only be called if you call them explicitly.
    def falls_in_rectangle(self, numx, numy):
        print("I am ordinary")
        if numx > self.x or numy > self.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def point(self):
        print(self.lowleft.x, self.lowleft.y, self.upright.x, self.upright.y)
        print(self.lowleft.x + self.lowleft.y + self.upright.x, self.upright.y)


point1 = Point(10, 20)
point2 = Point(1, 2)
# So when we create a Object Instance self is our Object.
print(point1.x, point1.y)

print(point1.falls_in_rectangle(9, 12))

print(point1.distance())

rec = Rectangle(Point(5, 6), Point(8, 9))
rec2 = Rectangle(Point(100, 100), Point(200, 200))
rec.point()
rec2.point()
