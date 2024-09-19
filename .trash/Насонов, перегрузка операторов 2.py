class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(f"v1 + v2 = {v3}")

v4 = v1 - v2
print(f"v1 - v2 = {v4}")

input()