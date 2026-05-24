from models import User
from storage import load_user, save_user


def show_menu() -> None:
    print("\n========================================")
    print("  HABIT TRACKER")
    print("========================================")
    print("1. Add habit")
    print("2. Mark habit for today")
    print("3. Today's habits")
    print("4. Streaks")
    print("5. List all habits")
    print("6. Delete habit")
    print("0. Exit")


def setup_user(user: User) -> None:
    """Ask for name on first run."""
    if not user.name or user.name == "Anonymous":
        name = input("Hello! What's your name? ").strip()
        if name:
            user.name = name


def cmd_add(user: User) -> None:
    name = input("Habit name: ").strip()
    try:
        user.add_habit(name)
        print(f"Habit '{name.lower()}' added.")
    except ValueError as e:
        print(f"Warning: {e}")


def cmd_check(user: User) -> None:
    name = input("Which habit did you complete? ").strip()
    try:
        print(user.check_habit(name))
    except KeyError as e:
        print(f"Warning: {e}")


def cmd_today(user: User) -> None:
    if not user.habits:
        print("No habits yet.")
        return
    print(f"\nToday ({user.name}):")
    for name, habit in user.habits.items():
        symbol = "[X]" if habit.done_today() else "[ ]"
        print(f"  {symbol} {name}")


def cmd_streaks(user: User) -> None:
    if not user.habits:
        print("No habits yet.")
        return
    print("\nStreaks:")
    for name, habit in user.habits.items():
        print(f"  {name}: {habit.streak()} days")


def cmd_list(user: User) -> None:
    if not user.habits:
        print("No habits yet.")
        return
    print("\nAll habits:")
    for name, habit in user.habits.items():
        print(f"  - {name}  (created: {habit.created}, checks: {len(habit.checks)})")


def cmd_remove(user: User) -> None:
    name = input("Which habit to delete? ").strip()
    if user.remove_habit(name):
        print(f"Habit '{name.lower()}' deleted.")
    else:
        print("Warning: habit not found.")


def main() -> None:
    user = load_user()
    setup_user(user)
    save_user(user)

    while True:
        show_menu()
        option = input("Option: ").strip()

        if option == "0":
            save_user(user)
            print("See you tomorrow!")
            break
        elif option == "1":
            cmd_add(user)
        elif option == "2":
            cmd_check(user)
        elif option == "3":
            cmd_today(user)
        elif option == "4":
            cmd_streaks(user)
        elif option == "5":
            cmd_list(user)
        elif option == "6":
            cmd_remove(user)
        else:
            print("Invalid option.")
            continue

        save_user(user)


if __name__ == "__main__":
    main()
