class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)


z = Vector(1, 2)
v = Vector(3, 4)
c = z + v
d = z - v
print(c.a, c.b)
print(d.a, d.b)

input()