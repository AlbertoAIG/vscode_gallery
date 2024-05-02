import reflex as rx
import vscode_plugins.styles.styles as styles
from vscode_plugins.routes import Route
from vscode_plugins.pages.index import index
from vscode_plugins.pages.themes import themes
from vscode_plugins.pages.formatters import formatters
from vscode_plugins.pages.debuggers import debuggers
from vscode_plugins.pages.testing import testing
from vscode_plugins.pages.others import others

class State(rx.State):
    "hola"

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="indigo", panel_background="translucent",
        class_name="background"
    )
)

app.add_page(themes)
app.add_page(formatters)
app.add_page(debuggers)
app.add_page(testing)
app.add_page(others)
