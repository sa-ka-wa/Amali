from sqlalchemy import column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Goal(Base):
    __tablename__ = 'goals'
    
    id = column(Integer, primary_key=True, index=True)
    user_id = column(Integer, index=True)
    goal_type = column(String, index=True)  # e.g., 'weight_loss', 'muscle_gain'
    target_value = column(Integer)  # e.g., target weight in kg
    current_value = column(Integer)  # e.g., current weight in kg
    start_date = column(String, default=datetime.utcnow().isoformat())
    end_date = column(String, nullable=True)  # Optional end date for the goal

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