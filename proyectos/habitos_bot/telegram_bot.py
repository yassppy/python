import os

from dotenv import load_dotenv
from models import User
from storage import load_user, save_user
from telegram.ext import Application, CommandHandler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

users: dict[str, User] = load_user()


def _get_user(update):
    """Returns the User if registered, None otherwise."""
    return users.get(str(update.effective_user.id))


async def start(update, context):
    user_id = str(update.effective_user.id)
    name = update.effective_user.first_name

    if user_id not in users:
        users[user_id] = User(user_id=user_id, name=name)
        save_user(users)
        reply = f"Hello {name}! You're now registered."
    else:
        reply = f"Welcome back {name}!"

    await update.message.reply_text(reply)


async def add_habit(update, context):
    """/add <name> — adds a new habit."""
    user = _get_user(update)
    if user is None:
        await update.message.reply_text("Please use /start first.")
        return
    if not context.args:
        await update.message.reply_text("Usage: /add <habit name>")
        return

    name = " ".join(context.args)
    try:
        user.add_habit(name)  # ← add_habit (inglés)
        save_user(users)
        await update.message.reply_text(f"Habit '{name.lower()}' added.")
    except ValueError as error:
        await update.message.reply_text(f"Warning: {error}")


async def mark_habit(update, context):
    """/mark <name> — marks a habit as done today."""
    user = _get_user(update)
    if user is None:
        await update.message.reply_text("Please use /start first.")
        return
    if not context.args:
        await update.message.reply_text("Usage: /mark <habit name>")
        return

    name = " ".join(context.args)
    try:
        message = user.check_habit(name)  # ← check_habit (inglés)
        save_user(users)
        await update.message.reply_text(message)
    except KeyError as error:
        await update.message.reply_text(f"Warning: {error}")


async def today(update, context):
    """/today — shows today's habit status."""
    user = _get_user(update)
    if user is None:
        await update.message.reply_text("Please use /start first.")
        return
    if not user.habits:  # ← habits (inglés)
        await update.message.reply_text("No habits registered yet.")
        return

    lines = ["Today's habits:"]
    for name, habit in user.habits.items():
        symbol = "[X]" if habit.done_today() else "[ ]"  # ← done_today()
        lines.append(f"  {symbol} {name}")

    await update.message.reply_text("\n".join(lines))


async def streaks(update, context):
    """/streaks — shows current streaks."""
    user = _get_user(update)
    if user is None:
        await update.message.reply_text("Please use /start first.")
        return
    if not user.habits:
        await update.message.reply_text("No habits registered yet.")
        return

    lines = ["Current streaks:"]
    for name, habit in user.habits.items():
        lines.append(f"  {name}: {habit.streak()} days")  # ← streak()

    await update.message.reply_text("\n".join(lines))


async def list_habits(update, context):
    """/list — lists all habits with details."""
    user = _get_user(update)
    if user is None:
        await update.message.reply_text("Please use /start first.")
        return
    if not user.habits:
        await update.message.reply_text("No habits registered yet.")
        return

    lines = ["All your habits:"]
    for name, habit in user.habits.items():
        lines.append(
            f"  - {name} (created: {habit.created}, checks: {len(habit.checks)})"
        )  # ← habit.created (inglés)

    await update.message.reply_text("\n".join(lines))


async def remove_habit(update, context):
    """/remove <name> — deletes a habit."""
    user = _get_user(update)
    if user is None:
        await update.message.reply_text("Please use /start first.")
        return
    if not context.args:
        await update.message.reply_text("Usage: /remove <habit name>")
        return

    name = " ".join(context.args)
    if user.remove_habit(name):  # ← remove_habit (inglés)
        save_user(users)
        await update.message.reply_text(f"Habit '{name.lower()}' deleted.")
    else:
        await update.message.reply_text("Warning: habit not found.")


async def help_command(update, context):
    """/help — shows available commands."""
    message = (
        "Available commands:\n"
        "/start — register\n"
        "/add <name> — add a habit\n"
        "/mark <name> — mark as done today\n"
        "/today — view today's status\n"
        "/streaks — view current streaks\n"
        "/list — list all habits\n"
        "/remove <name> — delete a habit\n"
        "/help — show this help"
    )
    await update.message.reply_text(message)


def main():
    if not TOKEN:
        print("Error: TELEGRAM_TOKEN not set in .env")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add_habit))
    app.add_handler(CommandHandler("mark", mark_habit))
    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("streaks", streaks))
    app.add_handler(CommandHandler("list", list_habits))
    app.add_handler(CommandHandler("remove", remove_habit))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot running. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
