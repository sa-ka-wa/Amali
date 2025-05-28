from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class FoodEntry(Base):
    __tablename__ = 'food_entries'
    
    id = Column(Integer, primary_key=True, index=True,nullable=False)
    user_id = Column(Integer, index=True)
    food_name = Column(String, index=True)
    calories = Column(Integer)
    protein = Column(Integer)
    carbs = Column(Integer)
    fats = Column(Integer)
    created_at = Column(String, default=datetime.utcnow().isoformat())

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
