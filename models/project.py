from config.database import Base
from sqlalchemy import Column, Integer, String, Text, Date

class ProjectModel(Base):

    __tablename__ = 'Project'

    Project_id = Column(Integer, primary_key=True)
    project = Column(String)
    description = Column(Text)
    status = Column(String)
    priority = Column(String)
    type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    goal_outcome = Column(Integer)
