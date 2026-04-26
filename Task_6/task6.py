class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"Woof! my Name is {self.name}")

class Calculator:
    def add(self,a,b):
        print(a+b)
    def subtract(self,a,b):
        print(a-b)
    def multiply(self,a,b):
        print(a*b)

class BankAccount:
    balance = 0
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance -=amount
            print(f"You withdrawed {amount}$, current balance is {self.balance}$")
        else:
            print(f"You don't have enough money, current balance is {self.balance}$")

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        print(self.height * self.width)

class Book:
    def __init__(self,title,author,is_available):
        self.title=title
        self.author=author
        self.is_available=is_available
    def borrow_book(self):
        if self.is_available == True:
            self.is_available=False
            print("You have burrowed the book")
        else:
            print("The book is already out")

