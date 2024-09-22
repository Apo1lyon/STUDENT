#Задание.Перезагрузка операторов 18.09.2024
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
# Создаем векторы
vector_a = Vector(2, 3)
vector_b = Vector(4, 5)

# Сложение векторов
result_add = vector_a + vector_b
print(result_add)  # Это вернет Vector(6, 8)

# Вычитание векторов
result_sub = vector_a - vector_b
print(result_sub)  # Это вернет Vector(-2, -2)

input()