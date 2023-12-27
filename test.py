import flet as ft
from PIL import Image


def main(page: ft.Page):
    page.title = "app"
    page.update()
    # Your code here


ft.app(target=main, assets_dir="assets")
