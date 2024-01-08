from config.database import Base
from sqlalchemy import Column, Integer, String, Text

class ValueGoalModel(Base):

    __tablename__ = 'ValueGoal'

    ValueGoal_id = Column(Integer, primary_key=True)
    value_goal = Column(String)
    description = Column(Text)
    status = Column(String)
    priority = Column(String)
    category = Column(String)
