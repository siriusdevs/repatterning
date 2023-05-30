# Написать класс PersonAttrsCreator, объект которого имеет два метода: 
# age() -> int возвращает случайный возраст от 0 до 100 
# name() -> str возвращает случайное имя 
# (можно использовать любой набор букв, где первая - заглавная, а можно использовать faker) 
# Использовать паттерн Синглтон (Singleton), 
# чтобы при работе программы всегда создавался только один экземпляр класса PersonAttrsCreator.


from random import randint, choice
from string import ascii_lowercase as letters

class PersonAttrsCreator:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def age(self) -> int:
        return randint(0, 100)

    def name(self) -> str:
        name = ''
        for _ in range(randint(5, 10)):
            name += choice(letters)
        return name.capitalize()

# 1.
creator = PersonAttrsCreator()
random_age = creator.age()
random_name = creator.name()
print(random_age)
print(random_name)
print(creator)

# 2.
creator2 = PersonAttrsCreator()
random_age2 = creator2.age()
random_name2 = creator2.name()
print(random_age2)
print(random_name2)
print(creator2)