from typing import Any, Dict, List, Optional, Tuple, Union

from dill.pointers import children
from kivy.core.window import WindowBase
from kivy.properties import (
    AliasProperty,
    BooleanProperty,
    NumericProperty,
    ObjectProperty,
    ReferenceListProperty,
    StringProperty,
)

from kivy.graphics import Canvas

WindowType = Union["Widget", "WindowBase"]
Numeric = Union[int, float]

class WidgetBase: ...

class Widget(WidgetBase):
    center_x: AliasProperty[int]
    center_y: AliasProperty[int]
    center: ReferenceListProperty[Tuple[int, int]]
    disabled: BooleanProperty
    height: NumericProperty[int]
    id: StringProperty
    opacity: NumericProperty[float]
    parent: ObjectProperty["Widget"] | "Widget"
    pos: ReferenceListProperty[Any] | Tuple[Numeric, Numeric]
    pos_hint: ObjectProperty[Dict[str, float]]
    right: AliasProperty[int]
    size: ReferenceListProperty[Tuple[int, int]] | Tuple[int, int]
    size_hint: ReferenceListProperty[Tuple[float | None, float | None]]
    size_hint_min: ReferenceListProperty[Tuple[float, float]]
    size_hint_max: ReferenceListProperty[Tuple[float, float]]
    size_hint_x: int | float | None
    size_hint_min_x: NumericProperty[int]
    size_hint_max_x: NumericProperty[int]
    size_hint_y: int | float | None
    size_hint_min_y: NumericProperty[int]
    size_hint_max_y: NumericProperty[int] | None
    top: AliasProperty[int]
    width: NumericProperty[int]
    x: int | float
    y: int | float
    children: List["Widget"]

    def __init__(
        self,
        size_hint_x: int | float | None = None,
        size_hint_y: int | float | None = None,
        size_hint: Optional[Tuple[Numeric | None, Numeric | None]] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        **kwargs: Any,
    ) -> None: ...
    def clear_widgets(self, children: Optional[List["Widget"]] = None) -> None: ...
    def collide_point(self, x: int, y: int) -> bool: ...
    def collide_widget(self, wid: "Widget") -> bool: ...
    def export_to_png(self, filename: str, flipped: Optional[bool] = False) -> None: ...
    def get_parent_window(self) -> WindowType: ...
    def get_root_window(self) -> WindowType: ...
    def remove_widget(self, widget: "Widget") -> None: ...
    def to_local(
        self, x: Numeric, y: Numeric, relative: Optional[bool] = False
    ) -> Tuple[Numeric, Numeric]: ...
    def to_parent(
        self, x: Numeric, y: Numeric, relative: Optional[bool] = False
    ) -> Tuple[Numeric, Numeric]: ...
    def to_widget(
        self, x: Numeric, y: Numeric, relative: Optional[bool] = False
    ) -> Tuple[Numeric, Numeric]: ...
    def to_window(
        self, x: Numeric, y: Numeric, relative: Optional[bool] = False
    ) -> Tuple[Numeric, Numeric]: ...
    def bind(self, **kwargs: Any) -> None: ...

    def add_widget(self, widget: Widget, index: int=0, canvas: Optional[Canvas]=None) -> None: ...