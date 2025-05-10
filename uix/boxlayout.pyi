from typing import Any, Dict, List, Optional, Tuple, Union

from kivy.graphics.instructions import Canvas
from kivy.properties import NumericProperty, ReferenceListProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget

numeric = Union[int, float, complex]

class BoxLayout(Layout):
    minimum_width: NumericProperty[float]
    minimum_height: NumericProperty[float]
    minimum_size: ReferenceListProperty[Tuple[int, int]]
    orientation: StringProperty
    spacing: NumericProperty[float]
    canvas: Canvas
    children: Tuple[Widget, ...]

    def __init__(
        self,
        orientation: Optional[str] = "horizontal",
        spacing: Optional[int] = 10,
        height: Optional[numeric] = None,
        width: Optional[numeric] = None,
        padding: Optional[
            Tuple[numeric, numeric]
            | Tuple[numeric, numeric, numeric, numeric]
            | numeric
        ] = None,
        size_hint: Optional[Tuple[float | None, float | None]] = None,
        pos_hint: Optional[Dict[str, float | int]] = None,
        size_hint_y: Optional[float | None] = None,
        size_hint_x: Optional[float | None] = None,
    ) -> None: ...
    def add_widget(
        self, widget: Layout | Widget | Label | TabbedPanel, *args: Any, **kwargs: Any
    ) -> None: ...
    def remove_widget(
        self, widget: Layout | Widget | Label | TabbedPanel, *args: Any, **kwargs: Any
    ) -> None: ...
    def bind(self, **kwargs: Any) -> None: ...
    def fbind(self, **kwargs: Any) -> None: ...

    def setter(
        self,
        value: Any
    ) -> None: ...
    def unbind(self, **kwargs: Any) -> None: ...
    def funbind(self, **kwargs: Any) -> None: ...
    def clear_widgets(self, children: Optional[List[Widget]] = None) -> None: ...