from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from ..database import Base

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), unique=True, nullable=False)
    avatar = Column(String(512), nullable=True)
    bio = Column(Text, nullable=True)
    level = Column(Integer, default=1)
    xp = Column(Float, default=0.0)
    credits = Column(Float, default=0.0)
    reputation = Column(Float, default=0.0)
    title = Column(String(100), nullable=True)

    user = relationship('User', back_populates='profile')
