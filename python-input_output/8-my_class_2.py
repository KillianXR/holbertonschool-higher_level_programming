#!/usr/bin/python3
class MyClass:
    """ My class """

    def __init__(self, name, number=4):
        self.__name = name        # Attribut privé
        self.number = number      # Attribut public
        self.is_team_red = (self.number % 2) == 0  # Booléen
        self.score = 0            # Score

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)
