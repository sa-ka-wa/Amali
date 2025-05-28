from models import Base, engine, SessionLocal, create_goal, get_goals_by_user, update_goal, delete_goal
from models import User  # Only if you're testing with a real user

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session
session = SessionLocal()

# Create a user to test with
new_user = User(username="testuser")
session.add(new_user)
session.commit()
session.refresh(new_user)
user_id = new_user.id

# CREATE
goal = create_goal(session, user_id=user_id, goal_type="muscle_gain", target_value=80, current_value=70)
print("Created:", goal)

# READ
goals = get_goals_by_user(session, user_id)
print("All goals for user:", goals)

# UPDATE
updated = update_goal(session, goal.id, current_value=72)
print("Updated goal:", updated)

# DELETE
deleted = delete_goal(session, goal.id)
print("Deleted:", deleted)
