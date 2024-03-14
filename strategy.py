from abc import ABC, abstractmethod
from enum import  Enum

class ChiefMood(Enum): # Класс наследуется от перечисления
    """Настроение начальника. Перечисление состояний"""
    GOOD = 1
    BAD = 2
    BETTER_STAY_AWAY = 3

class Strategy(ABC): #Интерфейс стратегия
    @abstractmethod
    def check_mood_chief(self,mood: ChiefMood) -> bool:
        pass

    @abstractmethod
    def order_processing(self, money: int) -> str:
        pass

class GoodStrategy(Strategy):
    def check_mood_chief(self,mood: ChiefMood) -> bool:
        if(mood is ChiefMood.GOOD or mood is ChiefMood.BAD)
            return True
        return  False

    def order_processing(self, money: int) -> str:
        return "Самый лучший напиток, который возможен!"

class BadStrategy(Strategy):
    def check_mood_chief(self,mood: ChiefMood) -> bool:
        return True

    def order_processing(self, money: int) -> str:
        if money < 5:
            return "Вежливо отказаться от заказа клиента"
        elif money < 10:
            return "Приготовить эспрессо"
        elif money < 20:
            return "Приготовить капучино"
        elif money < 50:
            return "Приготовить отменный кофе"
        else:
            return "Самый лучший напиток, который возможен!"

class Barista:
    def __init__(self,strategy: Strategy, chief_mood: ChiefMood):
        self._strategy = strategy
        self._chief_mood = chief_mood
        print(f"Изначальное настроение шефа: {chief_mood.name}")

    def get_chief_mood(self) -> ChiefMood:
        return self._chief_mood

    def set_chief_mood(self, chief_mood) -> None:
        print(f"Текущее настроение шефа: {chief_mood.name}")
        self._chief_mood = chief_mood
    
