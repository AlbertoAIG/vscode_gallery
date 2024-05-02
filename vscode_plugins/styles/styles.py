import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"
FADEIN_ANIMATION = "animate__animated animate__fadeIn"
BOUNCEIN_ANIMATION = "animate__animated animate__bounceIn"

# Sizes


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

# Sizes number


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"


class TipePlugin(Enum):
    THEMES = "Theme"
    FORMATTERS = "Formatter"
    DEBUGGERS = "Debugger"
    TESTING = "Testing"
    LANGUAGE = "Language"
    OTHERS = "Other"
    
# Styles


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,


    rx.menu.item: {
        "color": Color.PRIMARY.value,
    },

    rx.button: {
        "width": "150px",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.PRIMARY.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {"background_color": Color.HOVER.value}
    },

    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
        "font_size": Size.BIG.value,
    },

    rx.text: {
        "color": TextColor.HEADER.value,
        "font_size": Size.DEFAULT.value
    },

    rx.card: {
        "margin_x": "50px",
        "margin_y": "50px",
        "variant": "ghost",
        "border_radius": Size.DEFAULT.value,
        "class_name": "translucid",
        "min_width":"150px",
        "padding_x":Size.DEFAULT.value,
        "padding_y":Size.DEFAULT.value

    },
}

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css"
]

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value,
)

body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.ZERO.value,
)
