from core.character import Character
from core.die import Die


class CombatResolver:
    def __init__(self, die: Die) -> None:
        self._die = die

    def resolveCombat(self, attacker: Character, defender: Character) -> None:
        characterAttackRoll = attacker.attack(self._die)
        if self.isHit(characterAttackRoll, defender.armorClass):
            self.reduceHitPoints(defender, 1)

    def isHit(self, attackRole: int, defenderAC: int) -> bool:
        return attackRole >= defenderAC

    def reduceHitPoints(self, affectedCharacter, damagePoints):
        affectedCharacter.hitpoints = affectedCharacter.hitpoints - damagePoints
