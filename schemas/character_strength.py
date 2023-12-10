from pydantic import BaseModel, Field
from typing import Optional

class CharacterStrengthSchema(BaseModel):
    id: Optional[int] = None
    strength: str = Field(min_length=4, max_length=35)
    degree: str = Field(min_length=6, max_length=9)
    type: str = Field(min_length=7, max_length=13)
    description: str = Field(max_length=200)

    class Config:
        json_schema_extra = {
            'example': {
                'strength': 'Strength',
                'degree': 'Degree',
                'type': 'Type',
                'description': 'Description'
            }
        }