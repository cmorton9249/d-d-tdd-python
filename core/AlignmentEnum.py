from enum import Enum, unique


@unique
class AlignmentEnum(Enum):
    Good = 0
    Neutral = 1
    Evil = 2
