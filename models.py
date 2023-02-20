from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


# class UserDataModel(Base):
#     __tablename__ = "userdata"
#     id = Column(Integer, primary_key=True, index=True, nullable=True)
#     name = Column(String(50), index=True, nullable=True)
#     email = Column(String(100), index=True, nullable=True)
#     password = Column(String(100), index=True, nullable=True)
#     created_at = Column(DateTime, default=datetime.now)


class VHappyModel(Base):
    __tablename__ = "very_happy"
    index = Column(Integer, primary_key=True, index=True, nullable=True)
    employeeID = Column(String(10), index=True, nullable=True)
    rated_at = Column(DateTime, default=datetime.now)


class HappyModel(Base):
    __tablename__ = "happy"
    index = Column(Integer, primary_key=True, index=True, nullable=True)
    employeeID = Column(String(10), index=True, nullable=True)
    rated_at = Column(DateTime, default=datetime.now)


class NeutralModel(Base):
    __tablename__ = "neutral"
    index = Column(Integer, primary_key=True, index=True, nullable=True)
    employeeID = Column(String(10), index=True, nullable=True)
    rated_at = Column(DateTime, default=datetime.now)


class SadModel(Base):
    __tablename__ = "sad"
    index = Column(Integer, primary_key=True, index=True, nullable=True)
    employeeID = Column(String(10), index=True, nullable=True)
    rated_at = Column(DateTime, default=datetime.now)


class VSadModel(Base):
    __tablename__ = "very_sad"
    index = Column(Integer, primary_key=True, index=True, nullable=True)
    employeeID = Column(String(10), index=True, nullable=True)
    rated_at = Column(DateTime, default=datetime.now)
