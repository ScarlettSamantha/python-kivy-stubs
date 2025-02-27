from typing import Dict, Tuple
from kivy.uix.layout import Layout

class FloatLayout(Layout):
    def __init__(
        self,
        size_hint: Tuple[float | None, float | None],
        width: int,
        height: int,
        pos_hint: Dict[str, float],
        **kwargs,
    ): ...
