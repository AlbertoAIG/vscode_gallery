from enum import Enum

class Route(Enum):
    INDEX = "/"
    THEMES = "/themes"
    FORMATTERS = "/formatters"
    DEBUGGERS = "/debuggers"
    TESTING = "/testing"
    OTHERS = "/others"
