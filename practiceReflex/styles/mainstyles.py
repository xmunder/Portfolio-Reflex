import reflex as rx
from enum import Enum

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"
    VERY_BIG="4em"
    
class Color(Enum):
    PRIMARY="#161A30"
    SECONDARY="#31304D"
    TERTIARY="#B6BBC4"
    QUATERNARY="#F0ECE5"
    
class Space(Enum):
    SMALL="0.5em"
    MEDIUM="1em"
    BIG="2em"
    VERY_BIG="8em"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]


BASE_STYLE = {
    "background_color": Color.PRIMARY.value,
    "color": Color.QUATERNARY.value,
    "font_family": "Poppins",
    "font_weight": "500",
    rx.Button:{
        "width":"100%",
        "height":Size.VERY_BIG.value,
        "background_color": Color.SECONDARY.value,
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "_hover": {
            "background_color": Color.TERTIARY.value
        }
    }
}
