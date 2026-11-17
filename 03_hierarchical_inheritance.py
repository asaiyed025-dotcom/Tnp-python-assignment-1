class Shape:
    def show(self):
        print("This is a shape")


class Circle(Shape):
    def area(self, r):
        print("Circle area =", 3.14 * r * r)


class Rectangle(Shape):
    def area(self, l, w):
        print("Rectangle area =", l * w)


class Triangle(Shape):
    def area(self, b, h):
        print("Triangle area =", 0.5 * b * h)


Circle().area(5)
Rectangle().area(4, 5)
Triangle().area(4, 6)
