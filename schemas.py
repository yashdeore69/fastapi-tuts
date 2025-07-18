from datetime import date
from enum import Enum
from pydantic import BaseModel

class RizzUrlChoices(Enum):
    ULTRA = 'ultra'
    THIKTHAK = 'thikthak'
    DADDY = 'daddy'

class Huzz(BaseModel):
    title: str
    date_rizzed: date

class Boi(BaseModel):
    id: int
    name: str
    rizz: str
    huzz: list[Huzz] = []

