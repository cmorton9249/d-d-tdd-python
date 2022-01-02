from unittest import TestCase
from core.character import Character
from core.combatResolver import CombatResolver
from unittest.mock import Mock


class CombatResolverTests(TestCase):
    def setUp(self) -> None:
        self._attacker = Mock(wraps=Character())
        self._defender = Mock(wraps=Character())
        self._systemUnderTest = CombatResolver()
        return super().setUp()

    def test_combatResolver_manages_attacks_between_two_parties(self):
        self._systemUnderTest.resolveCombat(self._attacker, self._defender)

        self._attacker.attack.assert_called_once()

    def test_combatResolver_determines_hits(self):
        