#problem 1
class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"My name is {self.name}")
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        super().speak()
        print("woof")

#problem 2
class Classroom():
    def __init__(self):
        self.students=[]
    def add_student(self,name):
        Classroom.students.append(name)
    def count_students(self):
        print(len(Classroom.students))

#problem 3
class Flight():
    def __init__(self):
        self.passengers=[]
    def add_passenger(self,passenger_obj):
        if isinstance(passenger_obj,Passenger):
            self.passengers.append(passenger_obj)
        else: print(f"{passenger_obj} is not a passenger")
class Passenger():
    def __init__(self,name):
        self.name=name

#problem 4
class Player():
    def __init__(self,name,score):
        self.name=name
        self.score=score
class Team():
    def __init__(self):
        self.members=[]
    def add_player(self,player_object):
        if isinstance(player_object,Player):
            self.members.append(player_object)
        else: print(f"{player_object} is not a player")

#problem 5
from abc import ABCMeta , abstractmethod
class Shape(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def area(self):
        pass
        
def print_area(shape_object):
    if isinstance(shape_object, Shape):
        print(f"The area is {shape_object.area()} cm^2")
    else: print(f"{shape_object} is not a shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side **2
