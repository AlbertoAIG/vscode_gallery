import reflex as rx
from vscode_plugins.model.Plugin import Plugin
from vscode_plugins.styles.styles import Size,Spacing
from vscode_plugins.styles.colors import Color,TextColor


def plugin_card(plugin: Plugin) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading(
                plugin.name,
                color=TextColor.HEADER.value,                    
                padding_left=Size.SMALL.value,
                padding_right=Size.SMALL.value,
                ),

            rx.link(
                rx.image(
                    src=plugin.image,
                    border_radius=Size.DEFAULT.value,
                    width="100%",
                    height="auto",
                    margin_right=Size.DEFAULT.value,
                    alt=f"Imagen del plugin: {plugin.name}",
                ),
                href=plugin.url,
                is_external=True
            ),
            
            rx.vstack(
                rx.text(
                    plugin.description,
                    color=TextColor.HEADER.value,
                    padding_top=Size.SMALL.value,
                    padding_left=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                    size="1"
                )
            )
        ),
        min_width="300px",
        min_height="500px",
        max_width="400px",
        max_height="600px",
        margin_top=Size.DEFAULT.value,
        margin_bottom=Size.DEFAULT.value,
        margin_left=Size.DEFAULT.value,
        margin_right=Size.DEFAULT.value,
        padding_x=Size.DEFAULT.value,
        variant="ghost",
        class_name="translucid",
    )
