from typing import Any, Dict, Tuple
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

class Screen(RelativeLayout):
    manager: ScreenManager

    def __init__(
        self,
        size_hint: Tuple[float | None, float | None] | None = ...,
        width: int | None = ...,
        height: int | None = ...,
        pos_hint: Dict[str, float] | None = ...,
        **kwargs: Any,
    ): ...

class ScreenManager(FloatLayout):
    current: str

    def __init__(
        self,
        size_hint: Tuple[float | None, float | None] | None = ...,
        width: int | None = ...,
        height: int | None = ...,
        pos_hint: Dict[str, float] | None = ...,
        **kwargs: Any,
    ): ...
