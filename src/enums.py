from enum import Enum, auto


class Emotions(Enum):
    HAPPY = auto()
    SAD = auto()
    ANGRY = auto()
    GRUMPY = auto()


class GameOutcome(Enum):
    WIN = 0
    LOSE = 1
    DRAW = 2
