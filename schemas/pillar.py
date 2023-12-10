from pydantic import BaseModel, Field
from typing import Optional

class PillarSchema(BaseModel):
    id: Optional[int] = None
    pillar: str = Field(min_length=5, max_length=15)
    pillar_group: str = Field(min_length=5, max_length=15)

    class Config:
        json_schema_extra = {
            'example': {
                'pillar': 'Pillar',
                'pillar_group': 'Group',
            }
        }