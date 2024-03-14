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
        self._qb = QuackBehavior()
        self._fb = FlyBehavior()
        

    @abstractmethod
    def display(self):
        pass

    def perfomFly(self):
        self._fb.fly()
    
    def perfomQuack(self):
        self._qb.quack()

class MallardDuck (Duck):
    
    def __init__(self):
        self._fb = FlyWithWings()
        self._qb = Quack()

    def display(self):
        print('Im a real Mallard duck')


mallard = MallardDuck()
mallard.perfomFly()
mallard.perfomQuack()
