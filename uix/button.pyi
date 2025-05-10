from kivy.uix.label import Label

from typing import Callable, Optional, Tuple, Any

class Button(Label):
    on_press: Optional[Callable[..., Any]]
    on_release: Optional[Callable[..., Any]]
    background_color: Optional[Tuple[float, float, float, float]]

    def bind(
        self,
        on_release: Optional[Callable[..., Any]] = None,
        on_press: Optional[Callable[..., Any]] = None,
        size_hint: Optional[Tuple[int | None, int | None]] = None,
        size_hint_x: Optional[float] = None,
        size_hint_y: Optional[float] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        **kwargs: Any,
    ) -> None: ...
