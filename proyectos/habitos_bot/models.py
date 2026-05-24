from datetime import date, timedelta


class Habit:
    def __init__(self, name: str):
        self.name = name.lower().strip()
        self.created: str = date.today().isoformat()
        self.checks: list[str] = []

    def mark_today(self) -> bool:
        today = date.today().isoformat()
        if today in self.checks:
            return False
        self.checks.append(today)
        return True

    def done_today(self) -> bool:
        return date.today().isoformat() in self.checks

    def streak(self) -> int:
        if not self.checks:
            return 0
        sorted_dates = sorted(
            [date.fromisoformat(c) for c in self.checks], reverse=True
        )
        today = date.today()
        expected = today if sorted_dates[0] == today else today - timedelta(days=1)
        if sorted_dates[0] != expected:
            return 0
        count = 0
        for d in sorted_dates:
            if d == expected:
                count += 1
                expected -= timedelta(days=1)
            else:
                break
        return count


class User:
    def __init__(
        self, user_id: str = "local", name: str = "Anonymous"
    ):  # ← único cambio
        self.user_id = user_id
        self.name = name
        self.habits: dict[str, Habit] = {}

    def add_habit(self, name: str) -> None:
        clean = name.lower().strip()
        if not clean:
            raise ValueError("Name cannot be empty.")
        if clean in self.habits:
            raise ValueError(f"'{clean}' already exists.")
        self.habits[clean] = Habit(clean)

    def remove_habit(self, name: str) -> bool:
        clean = name.lower().strip()
        if clean not in self.habits:
            return False
        del self.habits[clean]
        return True

    def check_habit(self, name: str) -> str:
        clean = name.lower().strip()
        if clean not in self.habits:
            raise KeyError(f"Habit '{clean}' not found.")
        habit = self.habits[clean]
        if habit.mark_today():
            return f"✓ '{clean}' marked! Streak: {habit.streak()} days."
        return f"Already marked '{clean}' today."
