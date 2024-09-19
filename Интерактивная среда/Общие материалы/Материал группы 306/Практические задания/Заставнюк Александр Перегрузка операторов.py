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

a = Vector(8, 9)
b = Vector(10, 11)

print(f"Вектор a: {a}")
print(f"Вектор b: {b}")

c = a + b
print(f"a + b = {c}")

d = a - b
print(f"a - b = {d}")

input()
