import os
import sys
import subprocess

PYTHON_PATH = os.path.join("env", "bin", "python")

def clear():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(command):
    try:
        subprocess.run(
            [PYTHON_PATH, 'cli.py'] + command.split(),
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running command: {e}")
    input("\n✅ Press Enter to return to the menu...")

def main_menu():
    while True:
        clear()
        print("🍽️  Amali Calorie Tracker CLI")
        print("=============================\n")
        print("1. Add User")
        print("2. List Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Add Food Entry")
        print("6. List Food Entries")
        print("7. Update Food Entry")
        print("8. Delete Food Entry")
        print("9. Add Goal")
        print("10. List Goals")
        print("11. Update Goal")
        print("12. Delete Goal")
        print("13. Add Meal Plan")
        print("14. List Meal Plans")
        print("15. Update Meal Plan")
        print("16. Delete Meal Plan")

        print("Q. Quit\n")

        choice = input("👉 Select an option: ").strip().lower()

        if choice == '1':
            run_command('user add')
        elif choice == '2':
            run_command('user list')
        elif choice == '3':
            user_id = input("🆔 Enter User ID to update: ").strip()
            name = input("✏️  Enter new name (leave blank to skip): ").strip()
            email = input("📧 Enter new email (leave blank to skip): ").strip()

            command = f"user update {user_id}"
            if name:
                command += f" --name '{name}'"
            if email:
                command += f" --email '{email}'"
            run_command(command)

        elif choice == '4':
            user_id = input("🆔 Enter User ID to delete: ").strip()
            run_command(f"user delete {user_id}")

        elif choice == '5':
            run_command('foodentry add')
        elif choice == '6':
            run_command('foodentry list')
        elif choice == '7':
            entry_id = input("🆔 Enter Food Entry ID to update: ").strip()
            food = input("🍱 New food name (blank to skip): ").strip()
            calories = input("🔥 New calories (blank to skip): ").strip()
            protein = input("💪 New protein (blank to skip): ").strip()
            carbs = input("🍞 New carbs (blank to skip): ").strip()
            fats = input("🥑 New fats (blank to skip): ").strip()

            command = f"foodentry update {entry_id}"
            if food: command += f" --food-name '{food}'"
            if calories: command += f" --calories {calories}"
            if protein: command += f" --protein {protein}"
            if carbs: command += f" --carbs {carbs}"
            if fats: command += f" --fats {fats}"
            run_command(command)

        elif choice == '8':
            entry_id = input("🆔 Enter Food Entry ID to delete: ").strip()
            run_command(f"foodentry delete {entry_id}")

        elif choice == '9':
            run_command('goal add')
        elif choice == '10':
            run_command('goal list')
        elif choice == '11':
            goal_id = input("🆔 Enter Goal ID to update: ").strip()
            goal_type = input("🎯 New goal type (blank to skip): ").strip()
            target_value = input("🎯 New target value (blank to skip): ").strip()
            current_value = input("📊 New current value (blank to skip): ").strip()
            start_date = input("📅 New start date (YYYY-MM-DD) (blank to skip): ").strip()
            end_date = input("📅 New end date (YYYY-MM-DD) (blank to skip): ").strip()

            command = f"goal update {goal_id}"
            if goal_type: command += f" --goal-type '{goal_type}'"
            if target_value: command += f" --target-value {target_value}"
            if current_value: command += f" --current-value {current_value}"
            if start_date: command += f" --start-date '{start_date}'"
            if end_date: command += f" --end-date '{end_date}'"
            run_command(command)

        elif choice == '12':
            goal_id = input("🆔 Enter Goal ID to delete: ").strip()
            run_command(f"goal delete {goal_id}")

        elif choice == '13':
            run_command('mealplan add')
        elif choice == '14':
            run_command('mealplan list')
        elif choice == '15':
            mealplan_id = input("🆔 Enter Meal Plan ID to update: ").strip()
            name = input("📛 New plan name (blank to skip): ").strip()
            description = input("📝 New description (blank to skip): ").strip()
            date = input("📅 New date (YYYY-MM-DD or leave blank for today): ").strip()

            command = f"mealplan update {mealplan_id}"
            if name: command += f" --name '{name}'"
            if description: command += f" --description '{description}'"
            if date: command += f" --date '{date}'"
            run_command(command)

        elif choice == '16':
            mealplan_id = input("🆔 Enter Meal Plan ID to delete: ").strip()
            run_command(f"mealplan delete {mealplan_id}")


        elif choice == 'q':
            print("\n👋 Goodbye!")
            break
        else:
            input("❌ Invalid choice. Press Enter to continue...")

        

if __name__ == '__main__':
    main_menu()
