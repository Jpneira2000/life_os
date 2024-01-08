from config.database import Base
from sqlalchemy import Column, Integer, String, Text

class CharacterStrengthModel(Base):

    __tablename__ = 'CharacterStrength'

    CharacterStrength_id = Column(Integer, primary_key=True)
    character_strength = Column(String)
    strength_level = Column(String)
    type = Column(String)
    description = Column(Text)
