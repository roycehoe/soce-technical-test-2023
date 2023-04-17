from enum import Enum, auto
from typing import Union

from dotenv import dotenv_values

IS_DEV = False if dotenv_values(".env").get("IS_DEV") is None else True
