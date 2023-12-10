from config.database import Base
from sqlalchemy import Column, Integer, String

class PillarModel(Base):

    __tablename__ = 'pillars'

    id = Column(Integer, primary_key = True)
    pillar = Column(String)
    pillar_group = Column(String)