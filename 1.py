# Написать следующую структуру классов: 

# Есть класс Person, описывающий человека. У человека есть свойства: 
# 	name: str - имя 
# 	id: int – id 

# Есть класс Room, который описывает помещение. Оно имеет свойство: 
# 	name: str - название помещения. 
# 	Также у любого помещения есть скрытое свойство: 
# 	users: list[int], которое хранит список id всех людей, у которых есть допуск к этому помещению.  
# 	Редактируется этот список только с помощью внешних методов 
# 	add(person: Person) -> None и remove(person: Person) -> None, 
#   которые добавляют и удаляют людей в пользователи комнаты соответственно. 

# Использовать паттерн Заместитель (Proxy) и написать класс RoomAccess 
# со статическим 	методом get(person: Person, room: Room) -> None, 
# который выводит сообщение формата 
# “пользователю {name} [не] предоставлен доступ в комнату {room name}”. 


class Person:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id


class Room:
    def __init__(self, name: str):
        self.name = name
        self._users = []

    def add(self, person: Person) -> None:
        self._users.append(person.id)

    def remove(self, person: Person) -> None:
        self._users.remove(person.id)


class RoomAccess:
    @staticmethod
    def get(person: Person, room: Room) -> None:
        if person.id in room._users:
            print(f'Пользователю {person.name} предоставлен доступ в комнату "{room.name}".')
        else:
            print(f'You ({person.name}) shall not pass! В комнату "{room.name}".')


person1 = Person('Вася', 1)
person2 = Person('Петя', 2)
person3 = Person('Ватя', 3)
person4 = Person('Песя', 4)

room1 = Room('Комнатная комната')
room2 = Room('Вовсе не комната')

room1.add(person1)
room1.add(person2)
# А вот третьему не дано
room2.add(person4)

RoomAccess.get(person1, room1)
RoomAccess.get(person2, room1)
RoomAccess.get(person3, room2)
RoomAccess.get(person4, room2)