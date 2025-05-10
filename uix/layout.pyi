from typing import Any, Tuple

from kivy.graphics import Canvas
from kivy.graphics.context_instructions import Numeric
from kivy.properties import ReferenceListProperty
from kivy.uix.widget import Widget

class Layout(Widget):
    children: Tuple[Widget, ...]
    canvas: Canvas
    pos: ReferenceListProperty[Any] | Tuple[Numeric, Numeric]

    def add_widget(self, widget: Widget, *args: Any, **kwargs: Any) -> None: ...
    def remove_widget(self, widget: Widget, *args: Any, **kwargs: Any) -> None: ...
    def bind(self, **kwargs: Any) -> None: ...
    def fbind(self, **kwargs: Any) -> None: ...
    def do_layout(self, *kwargs: Any) -> None: ...
