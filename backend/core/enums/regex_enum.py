from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-Z][a-zA-Z]{1,19}$',
        'First letter uppercase min 2, max 20',
    )

    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])(\S){8,16}$',
        [
            'password must contain 1 number (0 - 9)',
            'password must contain min 1 uppercase letter',
            'password must contain min 1 lowercase letter',
            'password must contain min 1 alphanumeric character',
            'password min 8 max 16 characters without spaces',

        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
