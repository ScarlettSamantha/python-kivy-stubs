from typing import Sequence, Tuple

from kivy.graphics.context_instructions import Numeric
from kivy.graphics.instructions import VertexInstruction
from kivy.properties import ReferenceListProperty
from kivy.uix.boxlayout import numeric

class Rectangle(VertexInstruction):
    pos: Sequence[int] | Tuple[int, int] | ReferenceListProperty[Tuple[int, int]]
    size: Sequence[int] | Tuple[int, int] | ReferenceListProperty[Tuple[int, int]]

    def __init__(
        self,
        pos: Sequence[int] | Tuple[int, int] | ReferenceListProperty[Tuple[int, int]],
        size: Sequence[int] | Tuple[int, int] | ReferenceListProperty[Tuple[int, int]],
        source: str = "",
    ) -> None: ...
