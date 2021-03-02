from math import floor
from random import randint

class Character:
    def __init__(self) -> None:
        self.constitution = self.ability()
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def roll_d6(self, n:int) -> list:
        return [randint(1, 6) for _ in range(n)]

    def ability(self) -> int:
        # Roll 4 times and then remove the first smallest score.
        rolls = self.roll_d6(4)
        rolls.remove(min(rolls))
        return sum(rolls)
        # Or, in the practical sense, we could have just rolled 3 times instead
        # of 4 and avoid all the remove() logic.
        # return sum(self.roll_d6(3))

def modifier(constitution:int) -> int:
    return floor((constitution - 10) / 2)
