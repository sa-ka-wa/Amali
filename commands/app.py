import typer
from commands.foodentry import foodentry_app
from commands.goals import goal_app

app_app = typer.Typer()

app_app.add_typer(foodentry_app, name="foodentry")
app_app.add_typer(goal_app, name="goal")

