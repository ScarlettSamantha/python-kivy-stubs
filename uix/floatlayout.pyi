from typing import Dict, Optional, Tuple

from kivy.graphics import Canvas
from kivy.uix.layout import Layout

class FloatLayout(Layout):
    canvas: Optional[Canvas]

    def __init__(
        self,
        size_hint: Optional[Tuple[float | None, float | None]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        pos_hint: Optional[Dict[str, float]] = None,
        **kwargs,
    ): ...
