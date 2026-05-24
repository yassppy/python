import json
from pathlib import Path

from models import Habit, User

DATA_FILE = Path(__file__).parent / "data" / "users.json"  # plural


def load_user() -> dict[str, User]:  # ← retorna dict
    if not DATA_FILE.exists():
        return {}
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, KeyError):
        print("Warning: corrupted data, starting fresh.")
        return {}

    users: dict[str, User] = {}
    for user_id, info in data.items():
        user = User(user_id=user_id, name=info.get("name", "Anonymous"))
        for name, hdata in info.get("habits", {}).items():
            habit = Habit(name)
            habit.created = hdata["created"]
            habit.checks = hdata["checks"]
            user.habits[name] = habit
        users[user_id] = user

    return users


def save_user(users: dict[str, User]) -> None:  # ← recibe dict
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = {
        user_id: {
            "name": user.name,
            "habits": {
                name: {"created": h.created, "checks": h.checks}
                for name, h in user.habits.items()
            },
        }
        for user_id, user in users.items()
    }
    DATA_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
