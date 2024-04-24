from typing import Optional
import reflex as rx


class State(rx.State):
    opt: str | None = "bla"
    opt_2: Optional[str] = None


def index() -> rx.Component:
    return rx.input(value=State.opt)


app = rx.App()
app.add_page(index)
