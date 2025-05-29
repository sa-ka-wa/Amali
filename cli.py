import typer
from commands.user import user_app
from commands.goals import goal_app
from commands.app import app_app
from commands.foodentry import foodentry_app

print("✅ cli.py running with args:", __import__('sys').argv)


app = typer.Typer()

app.add_typer(user_app, name="user")
app.add_typer(app_app, name="app")
app.add_typer(foodentry_app, name="foodentry")
app.add_typer(goal_app, name="goal")

if __name__ == "__main__":
   app()
