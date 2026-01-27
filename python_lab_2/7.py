import math
# using normal formula
x = float(input("Enter base:- "))
y = float(input("Enter height:- "))

print("Area of the triangle:- ", 0.5 * x * y )

#OR Using Heron's formula
x = float(input("Enter first side:- "))
y = float(input("Enter second side:- "))
z = float(input("Enter third side:- "))

s = (x + y + z) / 2

area = math.sqrt(s * (s - x) * (s - y) * (s - z))
print ("Area:- ", area)