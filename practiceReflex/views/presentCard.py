import reflex as rx
from practiceReflex.styles.mainstyles import *
from practiceReflex.components.link_icons import *

def presentationCard() -> rx.Component:
    return rx.hstack(
        rx.avatar(
            size="xl",
            src="/cristianpic.png",
            background_color=Color.TERTIARY.value,
            border="solid",
            border_width="4px",
            margin_right=Size.SMALL.value + "!important",
        ),
        rx.vstack(
            rx.text(
                "Cristian Gómez",
                font_size="1.5em",
                font_weight="bold",
            ),
            rx.text(
                "Ingeniero Electrónico",
                color=Color.TERTIARY.value,
                margin_top="0px !important"
            ),
            rx.hstack(
                linkicon(
                    "/icons/github.svg",
                    "https://github.com/xmunder",
                    "GitHub Profile"
                ),
                linkicon(
                    "/icons/linkedin.svg",
                    "https://www.linkedin.com/in/cristian-camilo-gomez-fernandez/",
                    "LinKeDin Profile"
                ),
                linkicon(
                    "/icons/email.svg",
                    "mailto:gomezcristian676@gmail.com",
                    "email Profile"
                ),
                rx.link(
                    rx.button(
                        "Descargar CV",
                        color=Color.QUATERNARY.value,
                        alt="CV",
                        width="100%",
                        height="100%",
                    ),
                    href="https://uscoeduco-my.sharepoint.com/:b:/g/personal/u20201185364_usco_edu_co/EdSr5kNgRFRLr8q6XK1lbpgBfvwcDe8yjQqJblAAVFi3TQ?e=GnCdG4",
                    is_external=True,
                ),
            ),
            justify_content="flex-start",
            align_items="flex-start",
            width="100%",
        ),
        margin_top=Size.BIG.value,
        margin_bottom=Size.BIG.value,
        justify_content="flex-start",
        align_items="flex-start",
        width="100%",
    )
    
def presentation() -> rx.Component:
    return rx.box(
        rx.text(
        """ 
            Soy estudiante avanzado de Ingeniería Electrónica, caracterizado por mi responsabilidad y capacidad de adaptación. Mi fascinación por la programación me ha llevado a incursionar en nuevas tecnologías, centrándome en el desarrollo web. Inicié este viaje en el mundo de Python, mi lenguaje de programación preferido, utilizando el framework Reflex para confeccionar mi portafolio. Asimismo, estoy ampliando mis conocimientos en JavaScript y React.    
        """
        ),
        font_size="0.85em",
        width="100%",
        margin_bottom=Size.BIG.value + "!important",
    )