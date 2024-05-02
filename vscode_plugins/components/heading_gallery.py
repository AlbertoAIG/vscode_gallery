import reflex as rx

def heading_gallery(tipo:str) -> rx.Component:
    return rx.card(
        rx.heading(
            f"Estos son los {tipo} para VSCode recomenados por la comunidad:",
        ),
        variant="ghost",
        class_name="translucid",
    ),