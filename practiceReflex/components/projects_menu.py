import reflex as rx
from practiceReflex.components.link_icons import linkicon
from practiceReflex.styles.mainstyles import *

"""def projectMenu(name:str, description:str, link:str, alt:str) -> rx.Component:
    return rx.hstack(
        rx.popover(
            rx.popover_trigger(rx.button(name,width="40vw")),
            rx.popover_content(
                 rx.popover_header(description, font_size=Size.MEDIUM.value),
                rx.popover_body(description, font_size=Size.MEDIUM.value),
                rx.popover_footer(
                    linkicon("/icons/github.svg",link,alt),
                ),
                rx.popover_close_button(background_color="#ce5c64"),
                background_color=Color.SECONDARY.value,
                width="40vw",
            ),
        ),
        justify_content="start",
    )
"""
def projectMenu(name:str, title:str, description:str, link1:str, link2:str ,alt:str, icon_num:int) -> rx.Component:
    if (icon_num == 1):
        return rx.hstack(
            rx.popover(
                rx.popover_trigger(rx.button(name,width="40vw")),
                rx.popover_content(
                    rx.popover_header(title, font_size=Size.DEFAULT.value),
                    rx.popover_body(description, font_size=Size.MEDIUM.value),
                    rx.popover_footer(
                        rx.hstack(
                            linkicon("/icons/drive.svg",link1,alt),
                        )
                    ),
                    rx.popover_close_button(background_color="#ce5c64"),
                    background_color=Color.SECONDARY.value,
                    width="40vw",
                ),
            ),
            justify_content="start",
        )
    elif (icon_num == 2):
        return rx.hstack(
            rx.popover(
                rx.popover_trigger(rx.button(name,width="40vw")),
                rx.popover_content(
                    rx.popover_header(title, font_size=Size.DEFAULT.value),
                    rx.popover_body(description, font_size=Size.MEDIUM.value),
                    rx.popover_footer(
                        rx.hstack(
                            linkicon("/icons/github.svg",link1,alt),
                            linkicon("/icons/drive.svg",link2,alt),
                        )
                    ),
                    rx.popover_close_button(background_color="#ce5c64"),
                    background_color=Color.SECONDARY.value,
                    width="40vw",
                ),
            ),
            justify_content="start",
        )
        