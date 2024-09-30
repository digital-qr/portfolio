import reflex as rx

class FloatButton(rx.Component):
    library = "antd"
    tag= "FloatButton"
    icon = rx.image(src="/icons/whatsapp.svg")
    href= "https://wa.me/message/2FP74LDFRS33D1"
    target= "_blank"
    badge = { "dot": True } 

float_button = FloatButton.create
