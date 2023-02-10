from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    name = Column(String, nullable=False)
    connection_date = Column(DateTime, default=datetime.now, nullable=False)
    username = Column(String, primary_key=True, nullable=False)
    tg_id = Column(BigInteger, nullable=False)
    reports = relationship('Questions', backref='question', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return self.tg_id


class Questions(Base):
    __tablename__ = 'Questions'
    id = Column(Integer, primary_key=True)
    owner = Column(String, ForeignKey('Users.username'), nullable=False)
    date = Column(DateTime, default=datetime.now, nullable=False)
    message = Column(String, nullable=False)
    response = Column(String, nullable=False)

    def __repr__(self):
        return self.message
