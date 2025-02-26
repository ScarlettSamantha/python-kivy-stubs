from typing import Tuple
from kivy.uix.modalview import ModalView

from kivy.properties import ReferenceListProperty

class Popup(ModalView):
    size_hint: Tuple[float, float] | ReferenceListProperty[Tuple[float, float]]  # type: ignore

    def __init__(self, **kwargs): ...
