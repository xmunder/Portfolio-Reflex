"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from practiceReflex.views.presentCard import *
from practiceReflex.views.projects import *
from practiceReflex.views.habilities import *
import practiceReflex.styles.mainstyles as styles

class State(rx.State):
    """The app state."""
    pass


def index() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                presentationCard(),
                presentation(),
                menuProjects(),
                habilidades(),
                max_width="40vw",
                widht="100%",
                display=["flex","flex","flex","flex","flex"],
            ),
        ),
    )
    


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(index)
app.compile()
