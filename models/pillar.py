from config.database import Base
from sqlalchemy import Column, Integer, String

class PillarGroupModel(Base):

    __tablename__ = 'PillarGroup'

    PillarGroup_id = Column(Integer, primary_key=True)
    pillar_group = Column(String)

class PillarModel(Base):

    __tablename__ = 'Pillar'

    Pillar_id = Column(Integer, primary_key=True)
    group = Column(Integer)
