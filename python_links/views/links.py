import reflex as rx
from python_links.components.link_button import link_button
from python_links.components.title import title
import python_links.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Trabajos Recientes"),
        link_button("R&R Cells (DEMO)", 
                    "Página web de estructura completa, ideal para empresas",
                    "/icons/blog.svg",
                    const.TWITCH_URL,
                    ),
        link_button("YMink Lash Playas", 
                    "Sitio web ideal para mostrar productos de manera rapida y sencilla",
                    "/icons/blog.svg",
                    const.YOUTUBE_URL),
        link_button("Estética EBEYBE",
                    "Página web enfocada en el SEO y optimización",
                    "/icons/blog.svg",
                    const.DRAGON_API),
        link_button("Discord",
                    "El chat de la comunidad",
                    "/icons/discord.svg",
                    const.DISCORD_URL),
        title("Recursos y más"), # Recursos y más
        link_button("Dragon Ball Api", 
                    "Api de Dradon Ball",
                    "/icons/api.svg",
                    const.GITHUB_URL,
                    ),
        link_button("Blog MundoCode", 
                    "Noticias y más",
                    "/icons/blog.svg",
                    const.BLOG,
                    ),
        title("Contacto"),
        link_button("Email", 
                    "retired64@proton.me",
                    "/icons/email.svg",
                    "mailto:retired64@proton.me",
                    ),
        link_button("Portafolio", 
                    "Aqui encontrás más información sobre mi",
                    "/icons/portfolio.svg",
                    const.PORTFOLIO,
                    ),
        width="100%",
        spacing="2"
    )
