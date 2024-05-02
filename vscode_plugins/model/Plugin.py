import reflex as rx
from enum import Enum

class Type(Enum):
    THEME = "Theme"
    FORMATTERS = "Formatter"
    DEBUGGERS = "Debugger"
    TESTING = "Testing"
    OTHERS = "Other"

class Plugin(rx.Base):
    name: str
    description: str
    url: str
    image: str
    type: Type