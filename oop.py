# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.__age = None
#
#     def sett_age(self,new_age):
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             raise ValueError('age has to be more then 0')
#
#     @property
#     def get_age(self):
#         return self.__age
#
#
# person_one = Person('Igor')
# person_one.sett_age(-1)
# print(person_one.name, person_one.get_age)

# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         return "Im an animal"
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#
# class Cat(Animal):
#     def speak(self):
#         return "meow"
#
# dog = Dog("Buddy")
# cat = Cat("Kitty")
# print(dog.name, dog.speak())
# print(cat.name, cat.speak())

# from abc import abstractmethod, ABC
#
# @abstractmethod
# class Shape(ABC):
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height
#
#     def area(self):
#         result = self.height * self.weight
#         return result
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         result = self.radius * 2 # ne stal iskat tochnuyu formulu <3
#         return result
#
# rect = Rectangle(10, 5)
# circle = Circle(7)
# print(rect.area())
# print(circle.area())

class Vehicle:
    def __init__(self,model):
        self.model = model

    def move(self):
        return print('Vehicle is moving')

class Car(Vehicle):
    def move(self):
        return print('car is driving')

class Bicycle(Vehicle):
    def move(self):
        return print('bicycle')

def move(vehicle):
    return vehicle.move()




car = Car('Honda')
bike = Bicycle('hondaone')

move(bike)
move(car)