from sqlalchemy import column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class FoodEntry(Base):
    __tablename__ = 'food_entries'
    
    id = column(Integer, primary_key=True, index=True)
    user_id = column(Integer, index=True)
    food_name = column(String, index=True)
    calories = column(Integer)
    protein = column(Integer)
    carbs = column(Integer)
    fats = column(Integer)
    created_at = column(String, default=datetime.utcnow().isoformat())
    
    def __repr__(self):
        return f"<FoodEntry(id={self.id}, user_id={self.user_id}, food_name='{self.food_name}', calories={self.calories})>"