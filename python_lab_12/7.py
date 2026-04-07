class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"Point(x={self.x}, y={self.y})")

P1 = Point(10, 20)
P2 = Point(12, 15)

P3 = P1 + P2

print("\nPoint 1:")
P1.display()

print("Point 2:")
P2.display()

print("After Addition (P3 = P1 + P2):")
P3.display()