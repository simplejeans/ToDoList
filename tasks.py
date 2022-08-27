from sqlalchemy import Column, String, Integer, Date
from database import Base


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date)

    def __repr__(self):
        return f"{self.id}, {self.task}, {self.deadline}"
