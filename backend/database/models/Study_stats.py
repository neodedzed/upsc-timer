from sqlite3.dbapi2 import Timestamp
from sqlalchemy import BigInteger, Boolean, Column, DateTime, func
from database.db import Base


class Study_Time(Base):

    __tablename__ = "study_sessions"

    id = Column(BigInteger, primary_key=True, autoincrement= True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    is_running = Column(Boolean, nullable=True)
    finish_time = Column(DateTime(timezone=True), nullable=True)

    # def __repr__(self):
    #     return f"Study booty, {self.id}:{self.created_at}:{self.is_running}:{self.finish_time}"