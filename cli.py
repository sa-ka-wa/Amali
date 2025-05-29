import typer
from models.goal import create_goal, get_goals_by_user
from db.database import SessionLocal

app = typer.Typer()

@app.command()
def add(
    user_id: int, 
    goal_type: str, 
    target_value: int = 0,      # optional, defaults to 0
    current_value: int = 0      # optional, defaults to 0
):
    session = SessionLocal()
    goal = create_goal(session, user_id, goal_type, target_value, current_value)
    typer.echo(f"Goal added: {goal}")
    session.close()

@app.command()
def list(user_id: int):
    session = SessionLocal()
    goals = get_goals_by_user(session, user_id)
    if not goals:
        typer.echo("No goals found.")
    else:
        for goal in goals:
            typer.echo(f"- {goal}")
    session.close()

if __name__ == "__main__":
    app()
