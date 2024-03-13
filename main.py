from abc import ABC, abstractmethod, abstractproperty

class FlyBehavior (ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings (FlyBehavior):
    def fly(self):
        print('im flying')

class FlyNoWay (FlyBehavior):
    def fly(self):
        print('i cant fly')

class QuackBehavior (ABC):
    @abstractmethod
    def quack (self):
        pass

class Quack (QuackBehavior):
    def quack(self):
        print('Quack')

class MuteQuack (QuackBehavior):
    def quack(self):
        print('<< Silence >>')

class Squeack (QuackBehavior):
    def quack(self):
        print ('Squeack')

class Duck (ABC):

    def __init__(self):
        self.qb = QuackBehavior()
        self.fb = FlyBehavior()
        

    @abstractmethod
    def display(self):
        pass

    def perfomFly(self):
        self.fb.fly()
    
    def perfomQuack(self):
        self.qb.quack()

class MallardDuck (Duck):
    
    def __init__(self):
        self.fb = FlyWithWings()
        self.qb = Quack()

    def display(self):
        print('Im a real Mallard duck')


mallard = MallardDuck()
mallard.perfomFly()
mallard.perfomQuack()
