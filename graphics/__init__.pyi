from typing import Any
from kivy.graphics.instructions import *
from kivy.graphics.fbo import Fbo as Fbo
from kivy.graphics.context_instructions import *
from kivy.graphics.stencil_instructions import *
from kivy.graphics.vertex_instructions import *

class Line:
    def __init__(self, width: int | float, *args: Any, **kwargs: Any) -> None: ...
