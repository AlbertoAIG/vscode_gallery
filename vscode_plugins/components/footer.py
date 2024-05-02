import reflex as rx
import datetime
from vscode_plugins.styles.styles import Size, Spacing
from vscode_plugins.styles.colors import TextColor

def footer() -> rx.Component:
    return rx.center(

            rx.box(
                f"© {datetime.date.today().year} ",
                rx.text(
                    "Alberto Íñigo",
                    as_="span",
                    color=TextColor.FOOTER.value
                ),
                " v1.",
                padding_top=Size.DEFAULT.value
            ),
            font_size=Size.MEDIUM.value,

        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.SMALL.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value,
        width="100%",
        height="100%"
    )
    
    