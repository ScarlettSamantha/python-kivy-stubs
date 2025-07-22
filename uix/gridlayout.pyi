from typing import Any, List, Tuple

from kivy.uix.layout import Layout


class GridLayout(Layout):
    
    spacing: Tuple[int, ...] | List[int] | int 
    padding: Tuple[int, ...] | List[int] | int
    
    def do_layout(self, *largs: Any) -> None: ...