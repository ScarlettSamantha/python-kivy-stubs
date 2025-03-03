from typing import Dict, Optional, Tuple
from typing import Union
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.properties import NumericProperty, ReferenceListProperty, StringProperty
from kivy.graphics.instructions import Canvas

numeric = Union[int, float, complex]

class BoxLayout(Layout):
    minimum_width: NumericProperty
    minimum_height: NumericProperty
    minimum_size: ReferenceListProperty[Tuple[int, int]]
    orientation: StringProperty
    spacing: NumericProperty
    canvas: Canvas

    def __init__(
        self,
        orientation: Optional[str] = "horizontal",
        spacing: Optional[int] = 10,
        height: Optional[numeric] = None,
        width: Optional[numeric] = None,
        padding: Optional[
            Tuple[numeric, numeric] | Tuple[numeric, numeric, numeric, numeric]
        ] = None,
        size_hint: Optional[Tuple[float | None, float | None]] = None,
        pos_hint: Optional[Dict[str, float | int]] = None,
    ) -> None: ...
    def add_widget(self, widget: Layout | Widget | Label, *args, **kwargs) -> None: ...
    def remove_widget(
        self, widget: Layout | Widget | Label, *args, **kwargs
    ) -> None: ...
    def bind(self, **kwargs) -> None: ...
    def fbind(self, **kwargs) -> None: ...
