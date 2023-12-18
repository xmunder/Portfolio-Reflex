import reflex as rx

def habilidades() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Habilidades"),
            justify_content="flex-start",
            font_size="1.5em",
            font_weight="bold",
            width="100%",
        ),
        rx.vstack(
            rx.hstack(
                rx.image(src="/icons/html.svg",width="50px",height="50px"),
                rx.image(src="/icons/css.svg",width="50px",height="50px"),
                rx.image(src="/icons/js.svg",width="50px",height="50px"),
                rx.image(src="/icons/python.svg",width="50px",height="50px"),
                rx.image(src="/icons/git.svg",width="50px",height="50px"),
                rx.image(src="/icons/github.svg",width="50px",height="50px"),
                rx.image(src="https://avatars.githubusercontent.com/u/104714959?s=48&v=4",width="50px",height="50px"),
                justify_content="center",
            ),
            rx.hstack(
                rx.image(src="/icons/arduino.svg",width="50px",height="50px"), 
                rx.image(src="/icons/multisim.svg",width="50px",height="50px"),
                rx.image(src="/icons/matlab.svg",width="50px",height="50px"),
                rx.image(src="/icons/raspberry-pi.svg",width="50px",height="50px"),
                justify_content="center",
            ),
            align_items="center",
            justify_content="center",
            width="100%",   
        ),
        width="100%",
    )