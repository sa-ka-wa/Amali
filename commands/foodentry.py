import typer
from models.foodentry import FoodEntry,create_food_entry, delete_food_entry, update_food_entry
from db.database import get_db_session

foodentry_app = typer.Typer()

def get_active_user():
    try:
        with open(".active_user") as f:
            return int(f.read())
    except FileNotFoundError:
 # No active user file found, prompt for user ID interactively
        user_id = typer.prompt("No active user selected. Please enter user ID")
        # Optionally, save it for next time:
        with open(".active_user", "w") as f:
            f.write(str(user_id))
        return int(user_id)

@foodentry_app.command()
def list():
    user_id = get_active_user()
    session = get_db_session()
    entries = session.query(FoodEntry).filter(FoodEntry.user_id == user_id).all()
    
    if not entries:
        typer.echo(f"No food entries found for user {user_id}")
        return
    
    typer.echo(typer.style(f"Food entries for user {user_id}:", fg=typer.colors.GREEN, bold=True))

    for entry in entries:
     typer.echo(
        f"- {typer.style(entry.food_name, fg=typer.colors.CYAN)} "
        f"({typer.style(str(entry.calories), fg=typer.colors.YELLOW)} kcal) "
        f"[ID: {typer.style(str(entry.id), fg=typer.colors.MAGENTA)}]"
    )

@foodentry_app.command()
def add(
    food: str = None,
    calories: int = None,
    protein: int = 0,
    carbs: int = 0,
    fats: int = 0
):
    if food is None:
        food = typer.prompt("Enter food name")
    if calories is None:
        calories = typer.prompt("Enter calories", type=int)

    user_id = typer.prompt("Enter user ID")
    session = get_db_session()
    try:
        entry = create_food_entry(
            session,
            user_id=user_id,
            food_name=food,
            calories=calories,
            protein=protein,
            carbs=carbs,
            fats=fats
        )
        typer.secho(f"✅ Added food entry {entry.food_name} ({entry.calories} kcal) for user {user_id}", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"❌ Failed to add entry: {e}", fg=typer.colors.RED)
    finally:
        session.close()

@foodentry_app.command()
def delete(entry_id: int):
    session = get_db_session()
    try:
        success = delete_food_entry(session, entry_id)
        if success:
            typer.secho(f"🗑️ Deleted food entry {entry_id}", fg=typer.colors.GREEN)
        else:
            typer.secho(f"❌ Entry with ID {entry_id} not found.", fg=typer.colors.RED)
    finally:
        session.close()

@foodentry_app.command()
def update( entry_id: int,
    food_name: str = typer.Option(None, help="New food name"),
    calories: int = typer.Option(None, help="New calories"),
    protein: int = typer.Option(None, help="New protein"),
    carbs: int = typer.Option(None, help="New carbs"),
    fats: int = typer.Option(None, help="New fats")
):
    session = get_db_session()
    try:
        data = {}
        if food_name is not None: data["food_name"] = food_name
        if calories is not None: data["calories"] = calories
        if protein is not None: data["protein"] = protein
        if carbs is not None: data["carbs"] = carbs
        if fats is not None: data["fats"] = fats

        updated = update_food_entry(session, entry_id, **data)
        if updated:
            typer.secho(f"✏️ Updated food entry {entry_id}.", fg=typer.colors.CYAN)
        else:
            typer.secho(f"❌ Food entry with ID {entry_id} not found.", fg=typer.colors.RED)
    finally:
        session.close()