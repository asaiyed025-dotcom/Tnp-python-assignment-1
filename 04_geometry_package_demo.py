from geometry.circle import area, circumference
from geometry.rectangle import area as rectangle_area
from geometry.rectangle import perimeter

r = float(input("Enter radius: "))
l = float(input("Enter length: "))
w = float(input("Enter width: "))

print("Circle area =", area(r))
print("Circle circumference =", circumference(r))
print("Rectangle area =", rectangle_area(l, w))
print("Rectangle perimeter =", perimeter(l, w))
