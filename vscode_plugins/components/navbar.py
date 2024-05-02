import reflex as rx
import vscode_plugins.styles.styles as style
# import vscode_plugins.constants as const
from vscode_plugins.routes import Route
from vscode_plugins.styles.styles import Size as Size
from vscode_plugins.styles.colors import TextColor as TextColor
from vscode_plugins.styles.colors import Color as Color
from vscode_plugins.components.link_nav import link_nav
from vscode_plugins.components.menu_item import menu_item


def navbar(showInit=False) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("VSCode", as_="span", color=Color.PRIMARY.value),
                rx.text("Gallery", as_="span", color=Color.SECONDARY.value),
                style=style.navbar_title_style
            ),
            href=Route.INDEX.value,
            padding_x=Size.DEFAULT.value
        ),
        rx.menu.root(
            rx.menu.trigger(
                rx.button("Menu"),
                width="100px",
                background_color=Color.PRIMARY.value,
                hover=Color.SECONDARY.value
            ),
            rx.menu.content(
                rx.cond(
                    showInit,
                    menu_item("Inicio",Route.INDEX.value),
                ),                
                rx.cond(
                    showInit,
                    rx.menu.separator(class_name="separator"),
                ),
                menu_item("Theme",Route.THEMES.value),
                menu_item("Formatters", Route.FORMATTERS.value),
                menu_item("Debuggers", Route.DEBUGGERS.value),
                menu_item("Testing", Route.TESTING.value),
                menu_item("Others", Route.OTHERS.value),
                width="10rem",
                variant="soft",
                bg=Color.CONTENT.value,
                color_scheme="purple"
            ),
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        border_radius=Size.DEFAULT.value,
        width="100%",
        z_index="999",
        top="0"
    )
