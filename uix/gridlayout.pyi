from typing import Any

from menus.kivy.mixins.collidable import Layout


class GridLayout(Layout):
    
    def do_layout(self, *largs: Any) -> None: ...