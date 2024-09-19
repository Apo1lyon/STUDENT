#Задание.Переопределение класса 12.09.2024
class Animal:
    def make_sound(self):
        raise NotImplementedError("Метод should be overridden in subclasses")

class Dog(Animal):
    def make_sound(self):
        return "Гав!"

    def bring_ball(self):
        return "Собака приносит мячик!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

    def catching_mice(self):
        return "Кошка ловит мышей!"

# Создаем экземпляры
dog = Dog()
cat = Cat()

# Вызываем методы
print(dog.make_sound())       # Это вернет "Гав!"
print(dog.bring_ball())       # Это вернет "Собака приносит мячик!"

print(cat.make_sound())       # Это вернет "Мяу!"
print(cat.catching_mice())    # Это вернет "Кошка ловит мышей!"

input()