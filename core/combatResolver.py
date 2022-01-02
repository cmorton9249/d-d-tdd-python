from core.character import Character
from core.die import Die


class CombatResolver:
    def __init__(self) -> None:
        pass

    def resolveCombat(self, attacker: Character, defender: Character) -> None:
        die = Die()
        characterAttackRoll = attacker.attack(die)
