from core.character import Character


class CombatResolver:
    def __init__(self) -> None:
        pass

    def resolveCombat(self, attacker: Character, defender: Character) -> None:
        characterAttackRoll = attacker.attack()
