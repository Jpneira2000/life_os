from config.database import Base
from sqlalchemy import Column, Integer, String, Text

class IdentitySectionModel(Base):

    __tablename__ = 'IdentitySection'

    IdentitySection_id = Column(Integer, primary_key = True)
    section = Column(String)

class IdentityTagModel(Base):

    __tablename__ = 'IdentityTag'

    IdentityTag_id = Column(Integer, primary_key = True)
    tag = Column(String)

class IdentityContentModel(Base):

    __tablename__ = 'IdentityContent'

    IdentityContent_id = Column(Integer, primary_key = True)
    identity_section = Column(Integer)
    identity_tag = Column(Integer)
    content = Column(Text)
