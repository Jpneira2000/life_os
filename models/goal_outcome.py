from config.database import Base
from sqlalchemy import Column, Integer, String, Text, Date

class GoalOutcomeModel(Base):

    __tablename__ = 'GoalOutcome'

    GoalOutcome_id = Column(Integer, primary_key=True)
    goal_outcome = Column(String)
    description = Column(Text)
    status = Column(String)
    priority = Column(String)
    term = Column(String)
    goal_completition_target = Column(Date)
    goal_completition = Column(Date)
    value_goal = Column(Integer)
