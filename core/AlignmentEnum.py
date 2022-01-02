from enum import Enum, unique

@unique
class AlignmentEnum(Enum):
    Unset = 0
    Good = 1
    Neutral = 2
    Evil = 3
