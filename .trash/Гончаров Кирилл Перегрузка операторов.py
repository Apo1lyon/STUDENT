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


vector1 = Vector(2, 3)
vector2 = Vector(1, 4)

sum_vector = vector1 + vector2
diff_vector = vector1 - vector2

print(f"Сумма векторов: {sum_vector}")
print(f"Разность векторов: {diff_vector}")

input()
