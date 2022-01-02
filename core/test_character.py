from AlignmentEnum import AlignmentEnum
from character import Character


def test_character_can_get_and_set_name():
    systemUnderTest = Character()
    systemUnderTest.setName("Chris")

    assert systemUnderTest.getName() == "Chris"


def test_character_gets_an_alignment_good():
    systemUnderTest = Character()
    systemUnderTest.setAlignment(AlignmentEnum.Good)

    assert systemUnderTest.getAlignment() is AlignmentEnum.Good


def test_character_gets_an_alignment_neutral():
    systemUnderTest = Character()
    systemUnderTest.setAlignment(AlignmentEnum.Neutral)

    assert systemUnderTest.getAlignment() is AlignmentEnum.Neutral


def test_character_gets_an_alignment_evil():
    systemUnderTest = Character()
    systemUnderTest.setAlignment(AlignmentEnum.Evil)

    assert systemUnderTest.getAlignment() is AlignmentEnum.Evil


def test_character_gets_an_alignment_evil():
    systemUnderTest = Character()

    assert systemUnderTest.getAlignment() is AlignmentEnum.Unset


def test_character_has_AC_Default_10():
    systemUnderTest = Character()

    assert systemUnderTest.getArmorClass() == 10
