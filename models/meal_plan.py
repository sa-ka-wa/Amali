from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(String, default=datetime.utcnow().isoformat())

    user = relationship("User", back_populates="meal_plans")

    def __repr__(self):
        return f"<MealPlan(id={self.id}, user_id={self.user_id}, name='{self.name}')>"

# CREATE
def create_meal_plan(session, user_id, name, description=None, plan_date=None):
    meal_plan = MealPlan(
        user_id=user_id,
        name=name,
        description=description
    )
    session.add(meal_plan)
    session.commit()
    session.refresh(meal_plan)
    return meal_plan

# READ
def get_meal_plans_by_user(session, user_id):
    return session.query(MealPlan).filter(MealPlan.user_id == user_id).all()

# UPDATE
def update_meal_plan(session, plan_id, **kwargs):
    meal_plan = session.query(MealPlan).filter(MealPlan.id == plan_id).first()
    if not meal_plan:
        return None
    for key, value in kwargs.items():
        setattr(meal_plan, key, value)
    session.commit()
    return meal_plan

# DELETE
def delete_meal_plan(session, plan_id):
    meal_plan = session.query(MealPlan).filter(MealPlan.id == plan_id).first()
    if meal_plan:
        session.delete(meal_plan)
        session.commit()
        return True
    return False
