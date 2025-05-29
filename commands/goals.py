import typer
from models.goal import create_goal, get_goals_by_user,delete_goal,update_goal
from db.database import SessionLocal

goal_app = typer.Typer()

@goal_app.command()
def add(
    user_id: int = typer.Option(..., prompt="Enter user ID"),
    goal_type: str = typer.Option(..., prompt="Enter goal type"),
    target_value: int = typer.Option(0, prompt="Enter target value (default 0)", show_default=True),
    current_value: int = typer.Option(0, prompt="Enter current value (default 0)", show_default=True)
):
    session = SessionLocal()
    try:
        goal = create_goal(session, user_id, goal_type, target_value, current_value)
        typer.secho("\n✅ Goal successfully added!", fg=typer.colors.GREEN, bold=True)
        typer.secho(f"👤 User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA)
        typer.secho(f"🏁 Goal Type: {goal_type}", fg=typer.colors.BRIGHT_BLUE)
        typer.secho(f"🎯 Target: {target_value}", fg=typer.colors.CYAN)
        typer.secho(f"📊 Current: {current_value}", fg=typer.colors.YELLOW)

    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()


@goal_app.command()
def list(user_id: int = typer.Option(..., prompt="Enter user ID to list goals")):
    
    session = SessionLocal()
    try:
        goals = get_goals_by_user(session, user_id)
        typer.secho(f"\n🔍 Fetching goals for User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
        if not goals:
            typer.secho("⚠️ No goals found.", fg=typer.colors.RED, bold=True)
        else:
            typer.secho("📋 User Goals:", fg=typer.colors.CYAN, bold=True)
            for goal in goals:
                typer.secho(f"""
🆔 Goal ID: {goal.id}
👤 User: {goal.user.name if goal.user else 'Unknown'} (ID: {goal.user_id})
🏁 Type: {goal.goal_type}
🎯 Target: {goal.target_value}
📊 Current: {goal.current_value}
📅 Start: {goal.start_date}
🛑 End: {goal.end_date if goal.end_date else 'Not set'}
""")

            # rest of the success output
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()

@goal_app.command("update")
def update_goal_cmd(
    goal_id: int = typer.Option(..., prompt="Enter Goal ID"),
    goal_type: str = typer.Option(None, prompt="New goal type (leave blank to skip)", show_default=False),
    target_value: int = typer.Option(None, prompt="New target value (leave blank to skip)", show_default=False),
    current_value: int = typer.Option(None, prompt="New current value (leave blank to skip)", show_default=False),
    start_date: str = typer.Option(None, prompt="New start date (leave blank to skip)", show_default=False),
    end_date: str = typer.Option(None, prompt="New end date (leave blank to skip)", show_default=False)
):
    session = SessionLocal()
    try:
        update_data = {}
        if goal_type: update_data["goal_type"] = goal_type
        if target_value: update_data["target_value"] = target_value
        if current_value: update_data["current_value"] = current_value
        if start_date: update_data["start_date"] = start_date
        if end_date: update_data["end_date"] = end_date

        goal = update_goal(session, goal_id, **update_data)
        if goal:
            typer.secho("✅ Goal updated:", fg=typer.colors.GREEN)
            typer.echo(goal)
        else:
            typer.secho("❌ Goal not found.", fg=typer.colors.RED)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()

@goal_app.command("delete")
def delete_goal_cmd(goal_id: int = typer.Option(..., prompt="Enter Goal ID to delete")):
    session = SessionLocal()
    try:
        success = delete_goal(session, goal_id)
        if success:
            typer.secho("🗑️ Goal deleted successfully.", fg=typer.colors.GREEN)
        else:
            typer.secho("❌ Goal not found.", fg=typer.colors.RED)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()

if __name__ == "__main__":
    goal_app
