from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    ACTIVATE = (
        'activate',
        timedelta(hours=1)
    )

    RECOVERY = (
        'recovery',
        timedelta(minutes=10)
    )

    SOCKET = (
        'socket',
        timedelta(seconds=30)
    )

    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime
