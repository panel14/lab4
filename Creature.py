from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def is_dead(self):
        pass

    @abstractmethod
    def try_find(self):
        pass
