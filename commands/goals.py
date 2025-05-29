import typer
from models.goal import create_goal, get_goals_by_user
from db.database import SessionLocal

app = typer.Typer()

@app.command()
def add(
    user_id: int = typer.Option(..., prompt="Enter user ID"),
    goal_type: str = typer.Option(..., prompt="Enter goal type"),
    target_value: int = typer.Option(0, prompt="Enter target value (default 0)", show_default=True),
    current_value: int = typer.Option(0, prompt="Enter current value (default 0)", show_default=True)
):
    session = SessionLocal()
    goal = create_goal(session, user_id, goal_type, target_value, current_value)
    typer.secho("\n✅ Goal successfully added!", fg=typer.colors.GREEN, bold=True)
    typer.secho(f"👤 User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA)
    typer.secho(f"🏁 Goal Type: {goal_type}", fg=typer.colors.BRIGHT_BLUE)
    typer.secho(f"🎯 Target: {target_value}", fg=typer.colors.CYAN)
    typer.secho(f"📊 Current: {current_value}", fg=typer.colors.YELLOW)
    try:
        session = SessionLocal()
        goal = create_goal(session, user_id, goal_type, target_value, current_value)
        # rest of the success output
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()


@app.command()
def list(user_id: int = typer.Option(..., prompt="Enter user ID to list goals")):
    
    session = SessionLocal()
    goals = get_goals_by_user(session, user_id)
    typer.secho(f"\n🔍 Fetching goals for User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
    if not goals:
        typer.secho("⚠️ No goals found.", fg=typer.colors.RED, bold=True)
    else:
        typer.secho("📋 User Goals:", fg=typer.colors.CYAN, bold=True)
        for goal in goals:
            typer.secho(f"• {goal}", fg=typer.colors.BRIGHT_BLUE)
    try:
        session = SessionLocal()
        goal = create_goal(session, user_id, goal_type, target_value, current_value)
        # rest of the success output
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()

if __name__ == "__main__":
    app()
goal_app = app
