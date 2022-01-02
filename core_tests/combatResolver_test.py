from unittest import TestCase
from core.character import Character
from core.combatResolver import CombatResolver


class CombatResolverTests(TestCase):
    def setUp(self) -> None:
        self._attacker = Character()
        self._defender = Character()
        self._systemUnderTest = CombatResolver()
        return super().setUp()

    def combatResolver_manages_attacks_between_two_parties():
        assert True == True
