from sqlalchemy import column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
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
    
    def __repr__(self):
        return f"<Goal(id={self.id}, user_id={self.user_id}, goal_type='{self.goal_type}', target_value={self.target_value})>"