import reflex as rx
from vscode_plugins.styles.styles import Size as Size
from vscode_plugins.styles.colors import TextColor as TextColor
from vscode_plugins.styles.colors import Color as Color

def link_nav(title: str) -> rx.Component:
    return rx.link(
        rx.text(title, color=Color.PRIMARY.value),
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        underline="hover"
    )