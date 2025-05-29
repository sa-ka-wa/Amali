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
        print("7. Set Goal")
        print("8. View Goals")
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
            run_command('goal set')
        elif choice == '8':
            run_command('goal list')
        elif choice == 'q':
            print("\n👋 Goodbye!")
            break
        else:
            input("❌ Invalid choice. Press Enter to continue...")

if __name__ == '__main__':
    main_menu()
