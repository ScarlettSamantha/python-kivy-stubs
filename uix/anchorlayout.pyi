from typing import Dict, List, Optional, Tuple

from kivy.properties import OptionProperty, VariableListProperty
from kivy.uix.boxlayout import numeric
from kivy.uix.layout import Layout

class AnchorLayout(Layout):
    anchor_x: OptionProperty[str]
    anchor_y: OptionProperty[str]
    padding: VariableListProperty[int]

    def __init__(
        self,
        anchor_x: Optional[str] = "center",
        anchor_y: Optional[str] = "center",
        padding: Optional[List[int]] = [0, 0, 0, 0],
        size_hint: Optional[List[numeric | None] | Tuple[numeric | None, numeric | None]] = None,
        pos_hint: Optional[Dict[str, numeric]] = None,
        height: Optional[numeric] = None,
        width: Optional[numeric] = None,
    ) -> None: ...
