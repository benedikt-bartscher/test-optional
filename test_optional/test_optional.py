from typing import Optional
import reflex as rx


class State(rx.State):
    no_default: str
    str_default: str = "bla"
    opt_no_default: Optional[str]
    opt_str_default: Optional[str] = "bla"
    opt_none_default: Optional[str] = None


def index() -> rx.Component:
    return rx.vstack(
        # works fine
        rx.input(value=State.no_default),
        # works fine
        rx.input(value=State.str_default),
        # TypeError: Invalid var passed for prop value, expected type typing.Union[str, int, bool], got value opt_no_default of type typing.Optional[str].
        # rx.input(value=State.opt_no_default),
        # works fine
        rx.input(value=State.opt_str_default),
        # TypeError: Invalid var passed for prop value, expected type typing.Union[str, int, bool], got value opt_none_default of type typing.Optional[str].
        # rx.input(value=State.opt_none_default),
    )


app = rx.App()
app.add_page(index)
