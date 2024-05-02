import reflex as rx
import vscode_plugins.utils as utils
from vscode_plugins.components.navbar import navbar
from vscode_plugins.components.form import form
from vscode_plugins.styles.styles import Size as Size
from vscode_plugins.styles.colors import Color as Color
from vscode_plugins.components.footer import footer


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.card(
            rx.heading(
                "Bienvenidos a la Gallery de Plugins para VS Code de la Comunidad",
                margin_bottom=Size.DEFAULT.value
            ),
            rx.text(
                """Aquí podrás encontrar una galería de plugins para el IDE Visual Studio Code 
                    utilizados y recomendados por la comunidad.
                    Además podrás enviar tus propias recomendaciones para compartirlas con el resto.
                    Un portal en el se recopiralan los mejores plugins para customizar la visualización
                    de VS Code, para testing, debugging, packs de lenguajes de programación y muchos otros.
                    """
            ),
            variant="ghost",
            class_name="translucid",
        ),
        rx.card(
            rx.heading(
                "Recomienda un Plugin:",
            ),
            form(),
            variant="ghost",
            class_name="translucid"
        ),
        footer(),
        height="100%",
        width="100%",

    )
