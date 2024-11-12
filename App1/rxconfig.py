import reflex as rx
def index() -> rx.Component:
    return rx.container(
        #boton para cambiar el tema
        rx.color_mode.button(position="top-right"),
        
        rx.heading("Bienvenido Pc Store!", size="9",color="Red"),
        rx.hstack(
            rx.text(
                "Pc Store es una aplicación móvil diseñada para conectar a los amantes de las Pc con una alta tecnologia y opciones diferentes. Su nombre, Pc Store, Da a conocer los multiples tipos de pc , haciendo referencia a la calidad y precio de opciones que ofrece la aplicación",
                size="5", color="Red"
            ),
            rx.text( 
                """Pc Store es reconocidad por su calidad, precios y variedad de Pc .
Somos Computer Shop con más de 15 años de experiencia en Ventas de Equipos de cómputo de la línea Gamer, Laptops, Monitores, Placas Madre,componentes y 
precios justos"
 
""",
                size="5", color="Red"
            ),
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",color_scheme="Pink"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button("categoria",color_scheme="Pink"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="instagram"),color_scheme="Blue"),
                        href="https://instagram.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="facebook"),color_scheme="Pink"),
                        href="",
                        is_external=True,
                    ),
                ),
                rx.image(src="https://tse4.mm.bing.net/th?id=OIP.tigg31a3wTsRl-ar0pga7QHaE8&pid=Api&P=0&h=180"),
                rx.image(src="https://tse4.mm.bing.net/th?id=OIP.pRWDM3mDtd8o8-fYWZ4pxQHaE8&pid=Api&P=0&h=180"),
                rx.image(src="https://mui.today/__export/1679842735291/sites/mui/img/2023/03/26/habitos-de-alimentacion-saludable-foto-blog-151.jpeg_554688468.jpeg"),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        bg="#661FF2"
    ),
app = rx.App()
app.add_page(index)