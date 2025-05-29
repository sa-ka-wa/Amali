import typer
from models.goal import create_goal, get_goals_by_user
from models.user import create_user, get_users, update_user, delete_user
from db.database import SessionLocal

user_app = typer.Typer()

@user_app.command()
def add(
    name: str = typer.Option(..., prompt="Enter username"),
    email: str = typer.Option(..., prompt="Enter email")
):
    session = SessionLocal()
    try:
        user = create_user(session, name, email)
        typer.secho("✅ User successfully created!", fg=typer.colors.GREEN, bold=True)
        typer.secho(f"👤 Name: {user.name}", fg=typer.colors.BRIGHT_CYAN)
        typer.secho(f"📧 Email: {user.email}", fg=typer.colors.MAGENTA)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()
@user_app.command()
def list():
    session = SessionLocal()
    try:
        users = get_users(session)
        typer.secho(f"\n🔍 Fetching all users", fg=typer.colors.BRIGHT_MAGENTA, bold=True)
        if not users:
            typer.secho("⚠️ No users found.", fg=typer.colors.RED, bold=True)
        else:
            typer.secho("📋 User List:", fg=typer.colors.CYAN, bold=True)
            for user in users:
                typer.secho(f"• {user.name} ({user.email})", fg=typer.colors.BRIGHT_BLUE)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()

@user_app.command()
def update(
    user_id: int = typer.Argument(..., help="ID of the user to update"),
    name: str = typer.Option(None, help="New name for the user"),
    email: str = typer.Option(None, help="New email for the user")
):
    session = SessionLocal()
    try:
        updates = {}
        if name:
            updates['name'] = name
        if email:
            updates['email'] = email
        
        if not updates:
            typer.secho("⚠️ No update fields provided. Use --name or --email.", fg=typer.colors.YELLOW)
            return

        user = update_user(session, user_id, **updates)
        if user:
            typer.secho(f"✅ User updated successfully!", fg=typer.colors.GREEN)
            typer.secho(f"👤 Name: {user.name}", fg=typer.colors.BRIGHT_CYAN)
            typer.secho(f"📧 Email: {user.email}", fg=typer.colors.MAGENTA)
        else:
            typer.secho(f"⚠️ No user found with ID {user_id}.", fg=typer.colors.YELLOW)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()


@user_app.command()
def delete(
    user_id: int = typer.Argument(..., help="ID of the user to delete")
):
    session = SessionLocal()
    try:
        deleted = delete_user(session, user_id)
        if deleted:
            typer.secho(f"✅ User with ID {user_id} deleted.", fg=typer.colors.GREEN)
        else:
            typer.secho(f"⚠️ No user found with ID {user_id}.", fg=typer.colors.YELLOW)
    except Exception as e:
        typer.secho(f"❌ Error: {e}", fg=typer.colors.RED)
    finally:
        session.close()


if __name__ == "__main__":
    user_app()

