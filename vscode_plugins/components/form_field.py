import reflex as rx
from vscode_plugins.styles.colors import Color as Color
from vscode_plugins.styles.styles import Size as Size


def form_field(
        label: str,
        placeholder: str,
        message: str,
        multiline=False) -> rx.Component:
    return rx.form.field(
        rx.form.label(
            label,
            color=Color.PRIMARY.value,
        ),
        rx.cond(multiline,
                rx.text_area(
                    placeholder=placeholder,
                    name=placeholder,
                    required=True,
                    style={"background_color":"#1f1f1f"},
                    border_color="Gray",
                    max_length=450
                ),
                rx.form.control(
                    rx.input.input(
                        placeholder=placeholder,
                        name=placeholder,
                        required=True,
                        radius="large",
                        style={"background_color":"#1f1f1f"},
                        border_color="Gray"
                    ),
                    as_child=True
                )
        ),
        rx.form.message(
            message,
            match="valueMissing",
            style={"color":"#FFFFFF"}
        ),
        padding_top=Size.DEFAULT.value,
        padding_bottom=Size.DEFAULT.value,
    )
