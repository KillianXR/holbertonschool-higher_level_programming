#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    pass

    @abstractmethod
    def sound(self):
					   pass
    
class Cat(Animal):
            
    def sound(self):
            return "Meow"

class Dog(Animal):

    def sound(self):
            return "Bark"