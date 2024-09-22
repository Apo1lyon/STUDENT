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

class Bird(Animal):
    def make_sound(self):
        return "Чик-Чирик!"

    def can_fly(self):
        return "Птица умеет планировать по воздуху !"

# Создаем экземпляры
dog = Dog()
cat = Cat()
bird = Bird()
# Вызываем методы
print(dog.make_sound())       # Это вернет "Гав!"
print(dog.bring_ball())       # Это вернет "Собака приносит мячик!"

print(cat.make_sound())       # Это вернет "Мяу!"
print(cat.catching_mice())    # Это вернет "Кошка ловит мышей!"

print(bird.make_sound())       # Это вернет "Чик-Чирик!"
print(bird.can_fly())    # Это вернет "Птица умеет планировать по воздуху!"

input()