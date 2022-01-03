from unittest import TestCase
from core.character import Character
from core.combatResolver import CombatResolver
from core.die import Die
from unittest.mock import MagicMock, PropertyMock


class CombatResolverTests(TestCase):
    def setUp(self) -> None:
        self._attacker = MagicMock(wraps=Character())
        self._defender = MagicMock(wraps=Character())
        mockDie = MagicMock(wraps=Die())
        self._systemUnderTest = CombatResolver(mockDie)
        return super().setUp()

    def test_combatResolver_manages_attacks_between_two_parties(self):
        type(self._defender).armorClass = PropertyMock(return_value=0)
        self._systemUnderTest._die.roll.return_value = 0

        self._systemUnderTest.resolveCombat(self._attacker, self._defender)

        self._attacker.attack.assert_called_once()

    def test_combatResolver_knows_if_hit_high_roll(self):
        result = self._systemUnderTest.isHit(11, 1)

        assert result == True

    def test_combatResolver_knows_if_hit_same_roll(self):
        result = self._systemUnderTest.isHit(11, 11)

        assert result == True

    def test_combatResolver_knows_if_miss_low_roll(self):
        result = self._systemUnderTest.isHit(1, 20)

        assert result == False

    def test_combatResolver_can_reduce_hitpoints(self):
        self._defender.hitpoints = 10

        self._systemUnderTest.reduceHitPoints(self._defender, 1)

        assert self._defender.hitpoints == 9

    def test_combatResolver_reduces_hitpoints_of_defender_when_hit(self):
        self._defender.armorClass = 5
        self._defender.hitpoints = 10
        self._systemUnderTest._die.roll.return_value = 6

        self._systemUnderTest.resolveCombat(self._attacker, self._defender)

        assert self._defender.hitpoints == 9
