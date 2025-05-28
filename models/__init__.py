from db.database import engine, Base

from .foodentry import FoodEntry, create_food_entry, get_food_entries_by_user, update_food_entry, delete_food_entry
from .goal import Goal, create_goal, get_goals_by_user, update_goal, delete_goal
from .user import User, create_user, get_user_by_id, get_user_by_email, update_user, delete_user
from models.base import Base

Base.metadata.create_all(bind=engine)
