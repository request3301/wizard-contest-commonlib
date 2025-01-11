from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel


class SpellType(str, Enum):
    ACTIVE = 'ACTIVE'
    PASSIVE = 'PASSIVE'


class SpellBase(BaseModel):
    type_: SpellType
    name: str
    description: str
    manacost: int


class Spell(SpellBase):
    id: int


class WizardBase(BaseModel):
    name: str
    speed: int
    power: int


class Wizard(WizardBase):
    id: int
    spells: List[Spell]

    @property
    def rank(self) -> int:
        return self._manapool * self.speed * self.power

    @property
    def _manapool(self) -> int:
        return sum(spell.manacost for spell in self.spells)


class User(BaseModel):
    id: int
    wizards: List[Wizard]


class SpellCreate(SpellBase):
    pass


class WizardCreate(WizardBase):
    pass


class UserCreate(BaseModel):
    id: int
