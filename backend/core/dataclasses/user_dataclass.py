from dataclasses import dataclass
from datetime import datetime


@dataclass
class Profile:
    id: int
    name: str
    surname: str
    age: int
    created_at: datetime
    updated_at: datetime


@dataclass
class User:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: datetime
    created_at: datetime
    updated_at: datetime
    profile: Profile
