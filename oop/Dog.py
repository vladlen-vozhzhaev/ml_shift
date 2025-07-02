class Animal:
    breed = 'Дворняга'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        return 'Тишина'

class Dog(Animal):
    def bark(self):
        print(f"{self.name} - woof woof!")
    def speak(self):
        return 'Гав-гав!'

class Cat(Animal):
    def meow(self):
        print(f"{self.name} - meow meow!")
    def speak(self):
        return 'Мяю-мяу!'

cat = Cat('Барсик', 40)
print(cat.name)
print(cat.speak())