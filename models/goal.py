from .user import User
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime


from .base import Base


class Goal(Base):
    __tablename__ = 'goals'
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    goal_type = Column(String, index=True)  # e.g., 'weight_loss', 'muscle_gain'
    target_value = Column(Integer,nullable=False)  # e.g., target weight in kg
    current_value = Column(Integer,nullable=False)  # e.g., current weight in kg
    start_date = Column(String)
    end_date = Column(String)  # Optional end date for the goal

    user = relationship("User", back_populates="goals")

    def __repr__(self):
        return f"<Goal(id={self.id}, user_id={self.user_id}, goal_type='{self.goal_type}', target_value={self.target_value})>"
    
# CREATE
def create_goal(session, user_id, goal_type, target_value, current_value, start_date=None, end_date=None):
    goal = Goal(
        user_id=user_id,
        goal_type=goal_type,
        target_value=target_value,
        current_value=current_value,
        start_date=start_date or datetime.utcnow().isoformat(),
        end_date=end_date
    )
    session.add(goal)
    session.commit()
    session.refresh(goal)
    return goal
# READ
def get_goals_by_user(session, user_id):
    return session.query(Goal).filter(Goal.user_id == user_id).all()
# UPDATE
def update_goal(session, goal_id, **kwargs):
    goal = session.query(Goal).filter(Goal.id == goal_id).first()
    if not goal:
        return None
    for key, value in kwargs.items():
        setattr(goal, key, value)
    session.commit()
    return goal
# DELETE
def delete_goal(session, goal_id):
    goal = session.query(Goal).filter(Goal.id == goal_id).first()
    if goal:
        session.delete(goal)
        session.commit()
        return True
    return False
