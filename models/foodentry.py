from sqlalchemy import column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class FoodEntry(Base):
    __tablename__ = 'food_entries'
    
    id = column(Integer, primary_key=True, index=True,nullable=False)
    user_id = column(Integer, index=True)
    food_name = column(String, index=True)
    calories = column(Integer,nullable=False)
    protein = column(Integer,nullable=False)
    carbs = column(Integer,nullable=False)
    fats = column(Integer,nullable=False)
    created_at = column(String, default=datetime.utcnow().isoformat())

    user = relationship("User", back_populates="food_entries")
    
    def __repr__(self):
        return f"<FoodEntry(id={self.id}, user_id={self.user_id}, food_name='{self.food_name}', calories={self.calories})>"
    

    # CREATE
def create_food_entry(session, user_id, food_name, calories, protein, carbs, fats):
    entry = FoodEntry(
        user_id=user_id,
        food_name=food_name,
        calories=calories,
        protein=protein,
        carbs=carbs,
        fats=fats
    )
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return entry

# READ
def get_food_entries_by_user(session, user_id):
    return session.query(FoodEntry).filter(FoodEntry.user_id == user_id).all()

# UPDATE
def update_food_entry(session, entry_id, **kwargs):
    entry = session.query(FoodEntry).filter(FoodEntry.id == entry_id).first()
    if not entry:
        return None
    for key, value in kwargs.items():
        setattr(entry, key, value)
    session.commit()
    return entry

# DELETE
def delete_food_entry(session, entry_id):
    entry = session.query(FoodEntry).filter(FoodEntry.id == entry_id).first()
    if entry:
        session.delete(entry)
        session.commit()
        return True
    return False
