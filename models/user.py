from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

from .base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    created_at = Column(String, default=datetime.utcnow().isoformat())

    food_entries = relationship("FoodEntry", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    meal_plans = relationship("MealPlan", back_populates="user", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
    
# CREATE
def create_user(session, name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
# READ
def get_users(session):
    return session.query(User).all()
def get_user_by_id(session, user_id):
    return session.query(User).filter(User.id == user_id).first()
def get_user_by_email(session, email):
    return session.query(User).filter(User.email == email).first()
# UPDATE
def update_user(session, user_id, **kwargs):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    for key, value in kwargs.items():
        setattr(user, key, value)
    session.commit()
    return user
# DELETE
def delete_user(session, user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False