from typing import Dict, Optional, Tuple
from kivy.uix.layout import Layout

class FloatLayout(Layout):
    def __init__(
        self,
        size_hint: Optional[Tuple[float | None, float | None]],
        width: Optional[int] = None,
        height: Optional[int] = None,
        pos_hint: Optional[Dict[str, float]] = None,
        **kwargs,
    ): ...
