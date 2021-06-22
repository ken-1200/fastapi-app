
from sqlalchemy import Column, Integer, String, Text

from todo.database import Base


class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(128), index=True)
    text = Column(Text)
