from config.database import Base
from sqlalchemy import Column, Integer, String

class CharacterStrengthModel(Base):

    __tablename__ = 'character_strengths'

    id = Column(Integer, primary_key=True)
    strength = Column(String)
    degree = Column(String)
    type = Column(String)
    description = Column(String)
