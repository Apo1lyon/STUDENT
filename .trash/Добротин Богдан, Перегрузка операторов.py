class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def subtract(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

a = Vector(2, 3)
b = Vector(-1, 5)
print("Addition result:", a.add(b))
print("Subtraction result:", a.subtract(b))

input()