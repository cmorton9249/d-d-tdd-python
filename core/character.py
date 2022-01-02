from core.alignmentEnum import AlignmentEnum


class Character:
    def __init__(
        self, name="", alignment=AlignmentEnum.Unset, armorClass=10, hitpoints=5
    ):
        self._name = name
        self._alignment = alignment
        self._armorClass = armorClass
        self._hitpoints = hitpoints

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        self._name = value

    def get_alignment(self) -> AlignmentEnum:
        return self._alignment

    def set_alignment(self, value: AlignmentEnum):
        self._alignment = value

    def get_armorClass(self) -> int:
        return self._armorClass

    def set_armorClass(self, value):
        self._armorClass = value

    def get_hitpoints(self) -> int:
        return self._hitpoints

    def set_hitpoints(self, value: int):
        self._hitpoints = value

    name = property(get_name, set_name)
    alignment = property(get_alignment, set_alignment)
    armorClass = property(get_armorClass, set_armorClass)
    hitpoints = property(get_hitpoints, set_hitpoints)

    def attack(self, die) -> int:
        return die.roll()

    def isHit(self, attackRole: int) -> bool:
        return attackRole >= self.armorClass
