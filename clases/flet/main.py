import flet as ft
from views import UserView

def main(page: ft.Page):
    UserView(page)

if __name__ == "__main__":
    ft.run(main)