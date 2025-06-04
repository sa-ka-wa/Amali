import typer
from sqlalchemy.orm import Session
from db.database import get_db_session
from models.meal_plan import create_meal_plan, get_meal_plans_by_user, update_meal_plan, delete_meal_plan

app = typer.Typer(help="Manage meal plans")

# Create
@app.command()
def add(
    user_id: int = typer.Option(..., prompt=True),
    name: str = typer.Option(..., prompt=True),
    description: str = typer.Option("", prompt="Description (optional)")
):
    session: Session = get_db_session()
    try:
        plan = create_meal_plan(session, user_id, name, description)
        typer.secho("\n✅ Meal plan successfully added!", fg=typer.colors.GREEN, bold=True)
        typer.secho(f"👤 User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA)
        typer.secho(f"📛 Name: {name}", fg=typer.colors.BRIGHT_BLUE)
        typer.secho(f"📝 Description: {description if description else 'None'}", fg=typer.colors.CYAN)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()

# List
@app.command()
def list(user_id: int = typer.Option(..., prompt=True)):
    session: Session = get_db_session()
    try:
        plans = get_meal_plans_by_user(session, user_id)
        typer.secho(f"\n🔍 Fetching meal plans for User ID: {user_id}", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
        if not plans:
            typer.secho("⚠️ No meal plans found.", fg=typer.colors.RED, bold=True)
        else:
            typer.secho("📋 User Meal Plans:", fg=typer.colors.CYAN, bold=True)
            for plan in plans:
                typer.secho(f"""
🆔 Plan ID: {plan.id}
👤 User: {plan.user.name if plan.user else 'Unknown'} (ID: {plan.user_id})
📛 Name: {plan.name}
📝 Description: {plan.description if plan.description else 'None'}
📅 Created: {plan.created_at}
""")
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()
# Update
@app.command()
def update(
    plan_id: int = typer.Argument(...,  help="Meal plan ID to update"),
    name: str = typer.Option(None, help="New name"),
    description: str = typer.Option(None, help="New description"),
    date: str = typer.Option(None, help="New date in YYYY-MM-DD format")
):
    session: Session = get_db_session()
    try:
        update_data = {}
        if name: update_data["name"] = name
        if description: update_data["description"] = description
        if date: update_data["created_at"] = f"{date}T00:00:00"

        plan = update_meal_plan(session, plan_id, **update_data)
        if plan:
            typer.secho("✅ Meal plan updated:", fg=typer.colors.GREEN)
            typer.echo(plan)
        else:
            typer.secho("❌ Meal plan not found.", fg=typer.colors.RED)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()

# Delete
@app.command()
def delete(plan_id: int = typer.Option(..., prompt=True)):
    session: Session = get_db_session()
    try:
        success = delete_meal_plan(session, plan_id)
        if success:
            typer.secho("🗑️ Meal plan deleted successfully.", fg=typer.colors.GREEN)
        else:
            typer.secho("❌ Meal plan not found.", fg=typer.colors.RED)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()
meal_plan_app = app