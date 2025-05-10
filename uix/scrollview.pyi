from typing import Any

from kivy.uix.stencilview import StencilView

class ScrollView(StencilView):
    scroll_x: float
    scroll_y: float
    
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:...
    def _update_effect_y_bounds(self, *arg: Any) -> None: ...
