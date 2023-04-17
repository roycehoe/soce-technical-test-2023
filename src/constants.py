from enum import Enum, auto
from typing import Union

from dotenv import dotenv_values

IS_DEV = False if dotenv_values(".env").get("IS_DEV") is None else True

EXAMPLE_BASE_URL = "www.example.com"
EXAMPLE_ONE_TWO_DETAILS_PATH = "one/two/details"
EXAMPLE_ONE_TWO_DETAILS_DEFAULT_PARAMS = "?one=foo?two=bar?three=baz"

DESCRIPTIVE_URL = f"{EXAMPLE_BASE_URL}/{EXAMPLE_ONE_TWO_DETAILS_DEFAULT_PARAMS}{EXAMPLE_ONE_TWO_DETAILS_DEFAULT_PARAMS}"


IMPORTANT_FILE_PATH = "important.json"
IMPORTANT_FILE_TWO_PATH = "also_important.json"

TOKEN = "iamtypicallyverylongsothiswouldtakeupquiteabitofspace"

FIRST_MAGIC_NUMBER = 420
SECOND_MAGIC_NUMBER = 69


# Mappings are preferred over storing values in enums
# an enum is created here as an example, although enums should
# be stored in a separate folder


class CharacterClass(Enum):
    WARRIOR = auto()
    NINJA = auto()
    ARCHER = auto()
    TANK = auto()


DEFAULT_CHARACTER_MULTIPLIER: dict[CharacterClass, Union[float, int]] = {
    CharacterClass.WARRIOR: 1,
    CharacterClass.NINJA: 2,
    CharacterClass.ARCHER: 3,
    CharacterClass.TANK: 0.5,
}
