from db.database import engine, Base

from .foodentry import FoodEntry, create_food_entry, get_food_entries_by_user, update_food_entry, delete_food_entry
from .goal import Goal, create_goal, get_goals_by_user, update_goal, delete_goal
from .user import User, create_user, get_user_by_id, get_user_by_email, update_user, delete_user
from .meal_plan import MealPlan, create_meal_plan, get_meal_plans_by_user, update_meal_plan, delete_meal_plan

from models.base import Base

Base.metadata.create_all(bind=engine)
