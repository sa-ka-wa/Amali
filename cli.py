# import typer
# from models.goal import create_goal, get_goals_by_user
# from db.database import SessionLocal

# app = typer.Typer()

# def main_menu():
#     typer.secho("Welcome to the Calorie Tracker CLI!", fg=typer.colors.BRIGHT_CYAN, bold=True)
#     typer.secho("Please choose an option:", fg=typer.colors.BRIGHT_YELLOW)
#     typer.secho("1. Add Goal", fg=typer.colors.BRIGHT_GREEN)
#     typer.secho("2. List Goals", fg=typer.colors.BRIGHT_BLUE)
#     typer.secho("3. Exit", fg=typer.colors.BRIGHT_RED)
#     choice = typer.prompt("Enter your choice (1-3)", type=int)

#     return choice

# @app.command()
# def cli():
#     while True:
#         choice = main_menu()
        
#         if choice == 1:
#             user_id = typer.prompt("Enter user ID", type=int)
#             goal_type = typer.prompt("Enter goal type")
#             target_value = typer.prompt("Enter target value (default 0)", default=0, type=int)
#             current_value = typer.prompt("Enter current value (default 0)", default=0, type=int)

#             session = SessionLocal()
#             goal = create_goal(session, user_id, goal_type, target_value, current_value)
#             session.close()

#             typer.secho("\n✅ Goal successfully added!", fg=typer.colors.GREEN, bold=True)
#             typer.secho(f"👤 User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA)
#             typer.secho(f"🏁 Goal Type: {goal_type}", fg=typer.colors.BRIGHT_BLUE)
#             typer.secho(f"🎯 Target: {target_value}", fg=typer.colors.CYAN)
#             typer.secho(f"📊 Current: {current_value}", fg=typer.colors.YELLOW)

#         elif choice == 2:
#             user_id = typer.prompt("Enter user ID to list goals", type=int)

#             session = SessionLocal()
#             goals = get_goals_by_user(session, user_id)
#             session.close()

#             typer.secho(f"\n🔍 Fetching goals for User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
#             if not goals:
#                 typer.secho("⚠️ No goals found.", fg=typer.colors.RED, bold=True)
#             else:
#                 typer.secho("📋 User Goals:", fg=typer.colors.CYAN, bold=True)
#                 for goal in goals:
#                     typer.secho(f"• {goal}", fg=typer.colors.BRIGHT_BLUE)

#         elif choice == 3:
#             typer.secho("Exiting the CLI. Goodbye!", fg=typer.colors.BRIGHT_RED, bold=True)
#             break

#         else:
#             typer.secho("Invalid choice. Please try again.", fg=typer.colors.RED)


# def add
# if __name__ == "__main__":
import typer
from commands.user import user_app
from commands.app import app_app
from commands.foodentry import foodentry_app


app = typer.Typer()



app.add_typer(user_app, name="user")
app.add_typer(app_app, name="app")
app.add_typer(foodentry_app, name="foodentry")

if __name__ == "__main__":
   app()
