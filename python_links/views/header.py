import reflex as rx
from python_links.components.link_icon import link_icon
from python_links.components.info_text import info_text
from python_links.styles.styles import Size as Size
from python_links.styles.colors import TextColor as TextColor
from python_links.styles.colors import Color as Color
from python_links.styles.fonts import Font as Font
import python_links.constants  as const

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/perfil.jpg",
                name="MiguelRamos",
                fallbac="MR", 
                size="7", 
                radius="full",
                padding="2px",
                border="4px solid",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Miguel Ramos",
                    size= "7",
                ),
                rx.text(
                    "+52 663 322 5758",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/x-twitter.svg",
                        const.X_URL,
                    ),
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL
                    ),
                    spacing="4",
                    padding_top=Size.SMALL.value
                ),
                padding_top=Size.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing="4"
        ),
        rx.flex(
            info_text("+7", "Sitios web"),
            rx.spacer(),
            info_text("+3", "Menus Digitales creados"),
            rx.spacer(),
            info_text("+549", "Seguidores"),
            width="100%",
        ),
        rx.text(
            "¡Impulsa tu negocio al siguiente nivel con una página web profesional y personalizada! Como creador y desarrollador de sitios web estáticos completos, te ofrezco una solución ideal para hacer crecer tu negocio y automatizar tus ventas. Con un formulario integrado, podrás reducir el tiempo de asesoría a tus clientes, facilitando ventas rápidas y efectivas. Muestra tu catálogo al mundo de una manera única y profesional. No pierdas más oportunidades de venta, ¡haz que tu negocio destaque con un sitio web que trabaje por ti las 24 horas!.",
            color=TextColor.BODY.value,
            font_size=Size.DEFAULT.value,
        ),
        spacing="4",
        align_items="start",
        width="100%"
    )
