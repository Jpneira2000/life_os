from config.database import Base
from sqlalchemy import Column, Integer, String, Text

class MindsetSectionModel(Base):

    __tablename__ = 'MindsetSection'

    MindsetSection_id = Column(Integer, primary_key = True)
    section = Column(String)

class MindsetTagModel(Base):

    __tablename__ = 'MindsetTag'

    MindsetTag_id = Column(Integer, primary_key = True)
    tag = Column(String)

class MindsetPhraseModel(Base):

    __tablename__ = 'MindsetPhrase'

    MindsetPhrase_id = Column(Integer, primary_key = True)
    mindset_section = Column(Integer)
    mindset_tag = Column(Integer)
    phrase = Column(Text)
    author = Column(String)
