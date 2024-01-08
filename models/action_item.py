from config.database import Base
from sqlalchemy import Column, Integer, String, Text, Date, Boolean

class ActionItemModel(Base):

    __tablename__ = 'ActionItem'

    ActionItem_id = Column(Integer, primary_key=True)
    description = Column(Text)
    priority = Column(String)
    status = Column(String)
    do_date = Column(Date)
    due_date = Column(Date)
    character_strength = Column(Integer)
    done = Column(Boolean)
    project = Column(Integer)
