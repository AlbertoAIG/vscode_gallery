import reflex as rx
from vscode_plugins.styles.colors import Color as Color

def menu_item(title: str, url: str) -> rx.Component:
    return rx.menu.item(
        rx.link(
            title,
            color="white",
            href=url
        )
    )