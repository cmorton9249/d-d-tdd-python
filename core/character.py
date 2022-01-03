from core.alignmentEnum import AlignmentEnum


class Character:
    def __init__(
        self, name="", alignment=AlignmentEnum.Unset, armorClass=10, hitpoints=5
    ):
        self._name = name
        self._alignment = alignment
        self._armorClass = armorClass
        self._hitpoints = hitpoints

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def alignment(self) -> AlignmentEnum:
        return self._alignment

    @alignment.setter
    def alignment(self, value: AlignmentEnum) -> None:
        self._alignment = value

    @property
    def armorClass(self) -> int:
        return self._armorClass

    @armorClass.setter
    def armorClass(self, value) -> None:
        self._armorClass = value

    @property
    def hitpoints(self) -> int:
        return self._hitpoints

    @hitpoints.setter
    def hitpoints(self, value: int) -> None:
        self._hitpoints = value

    def attack(self, die) -> int:
        return die.roll()
