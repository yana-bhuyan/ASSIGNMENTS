import math
a, b, c = 1,-3, 2
d = b*b- 4*a*c
if d > 0:
 r1 = (-b + math.sqrt(d)) / (2*a)
 r2 = (-b- math.sqrt(d)) / (2*a)
 print(r1, r2)
elif d == 0:
 r =-b / (2*a)
 print(r)
else:
 print("Imaginary roots")