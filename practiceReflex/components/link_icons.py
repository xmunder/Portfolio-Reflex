import reflex as rx

def linkicon(image: str, url:str, alt:str) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.image(
                src=image,
                alt = alt,
                width="24px",
                height="24px",
            ),
            href=url,
            is_external=True,
        ),
    )