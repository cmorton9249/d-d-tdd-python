from unittest import TestCase
from core.character import Character
from core.die import Die
from core.alignmentEnum import AlignmentEnum
from unittest.mock import patch


class CharacterTests(TestCase):
    def setUp(self) -> None:
        self._systemUnderTest = Character()
        return super().setUp()

    def test_character_can_get_and_set_name(self):
        self._systemUnderTest.name = "Chris"

        assert self._systemUnderTest.name == "Chris"

    def test_character_gets_an_alignment_good(self):
        self._systemUnderTest.alignment = AlignmentEnum.Good

        assert self._systemUnderTest.alignment is AlignmentEnum.Good

    def test_character_gets_an_alignment_neutral(self):
        self._systemUnderTest.alignment = AlignmentEnum.Neutral

        assert self._systemUnderTest.alignment is AlignmentEnum.Neutral

    def test_character_gets_an_alignment_evil(self):
        self._systemUnderTest.alignment = AlignmentEnum.Evil

        assert self._systemUnderTest.alignment is AlignmentEnum.Evil

    def test_character_gets_an_alignment_evil(self):
        assert self._systemUnderTest.alignment is AlignmentEnum.Unset

    def test_character_has_AC_Default_10(self):
        assert self._systemUnderTest.armorClass == 10

    def test_character_can_set_ac(self):
        self._systemUnderTest.armorClass = 1

        assert self._systemUnderTest.armorClass == 1

    @patch("core.die")
    def test_Character_can_attack(self, mockDie):
        mockDie.roll.return_value = 15

        attackRoll = self._systemUnderTest.attack(mockDie)

        assert attackRoll == 15


