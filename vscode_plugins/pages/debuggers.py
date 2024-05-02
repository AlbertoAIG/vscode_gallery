import reflex as rx
import vscode_plugins.utils as utils
from vscode_plugins.components.navbar import navbar
from vscode_plugins.components.plugin_card import plugin_card
from vscode_plugins.styles.styles import Size, Spacing
from vscode_plugins.styles.colors import Color as Color
from vscode_plugins.state.PageState import PageState
from vscode_plugins.routes import Route
from vscode_plugins.components.footer import footer
from vscode_plugins.components.heading_gallery import heading_gallery


@rx.page(
    route=Route.DEBUGGERS.value,
    title=utils.debugger_title,
    description=utils.debugger_description,
    image=utils.preview,
    meta=utils.debugger_meta,
    on_load=PageState.plugin_links("Debugger")
)
def debuggers() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(showInit=True),
        heading_gallery("Debuggers"),
        rx.box(
            rx.cond(
                PageState.plugin_info,
                rx.vstack(
                    rx.flex(
                        rx.center(
                            rx.foreach(
                                PageState.plugin_info,
                                plugin_card
                            ),
                            flex_direction=["column", "row"],
                            flex_wrap="wrap",
                            spacing=Spacing.DEFAULT.value,
                            width="100%"
                        ),
                        width="100%",
                        padding_x="7%",
                    ),
                )
            ),
        ),
        footer(),
        height="100%",
        width="100%",
    )
