from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Boolean
)

from .meta import Base


class BasicInfo(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    password = Column(Text)
    email = Column(Text)
    n_exercises = Column(Integer)

# Index('my_index', BasicInfo.name, unique=True, mysql_length=255)
