"""
This type stub file was generated by pyright.
"""

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

'''
FileChooser
===========

The FileChooser module provides various classes for describing, displaying and
browsing file systems.

Simple widgets
--------------

There are two ready-to-use widgets that provide views of the file system. Each
of these present the files and folders in a different style.

The :class:`FileChooserListView` displays file entries as text items in a
vertical list, where folders can be collapsed and expanded.

.. image:: images/filechooser_list.png

The :class:`FileChooserIconView` presents icons and text from left to right,
wrapping them as required.

.. image:: images/filechooser_icon.png

They both provide for scrolling, selection and basic user interaction.
Please refer to the :class:`FileChooserController` for details on supported
events and properties.

Widget composition
------------------

FileChooser classes adopt a
`MVC <https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller>`_
design. They are exposed so that you to extend and customize your file chooser
according to your needs.

The FileChooser classes can be categorized as follows:

* Models are represented by concrete implementations of the
  :class:`FileSystemAbstract` class, such as the :class:`FileSystemLocal`.

* Views are represented by the :class:`FileChooserListLayout` and
  :class:`FileChooserIconLayout` classes. These are used by the
  :class:`FileChooserListView` and :class:`FileChooserIconView` widgets
  respectively.

* Controllers are represented by concrete implementations of the
  :class:`FileChooserController`, namely the :class:`FileChooser`,
  :class:`FileChooserIconView` and :class:`FileChooserListView` classes.

This means you can define your own views or provide :class:`FileSystemAbstract`
implementations for alternative file systems for use with these widgets.
The :class:`FileChooser` can be used as a controller for handling multiple,
synchronized views of the same path. By combining these elements, you can add
your own views and file systems and have them easily interact with the existing
components.

Usage example
-------------

main.py

.. include:: ../../examples/RST_Editor/main.py
    :literal:

editor.kv

.. highlight:: kv

.. include:: ../../examples/RST_Editor/editor.kv
    :literal:

.. versionadded:: 1.0.5

.. versionchanged:: 1.2.0

    In the chooser template, the `controller` is no longer a direct reference
    but a weak-reference. If you are upgrading, you should change the notation
    `root.controller.xxx` to `root.controller().xxx`.

'''
__all__ = ('FileChooserListView', 'FileChooserIconView', 'FileChooserListLayout', 'FileChooserIconLayout', 'FileChooser', 'FileChooserController', 'FileChooserProgressBase', 'FileSystemAbstract', 'FileSystemLocal')
platform = ...
filesize_units = ...
_have_win32file = ...
if platform == 'win':
    _have_win32file = ...
def alphanumeric_folders_first(files, filesystem): # -> list[Any]:
    ...

class FileSystemAbstract:
    '''Class for implementing a File System view that can be used with the
    :class:`FileChooser <FileChooser>`.

    .. versionadded:: 1.8.0
    '''
    def listdir(self, fn): # -> None:
        '''Return the list of files in the directory `fn`
        '''
        ...
    
    def getsize(self, fn): # -> None:
        '''Return the size in bytes of a file
        '''
        ...
    
    def is_hidden(self, fn): # -> None:
        '''Return True if the file is hidden
        '''
        ...
    
    def is_dir(self, fn): # -> None:
        '''Return True if the argument passed to this method is a directory
        '''
        ...
    


class FileSystemLocal(FileSystemAbstract):
    '''Implementation of :class:`FileSystemAbstract` for local files.

    .. versionadded:: 1.8.0
    '''
    def listdir(self, fn):
        ...
    
    def getsize(self, fn): # -> int:
        ...
    
    def is_hidden(self, fn): # -> bool:
        ...
    
    def is_dir(self, fn): # -> bool:
        ...
    


class FileChooserProgressBase(FloatLayout):
    '''Base for implementing a progress view. This view is used when too many
    entries need to be created and are delayed over multiple frames.

    .. versionadded:: 1.2.0
    '''
    path = ...
    index = ...
    total = ...
    def cancel(self, *largs): # -> None:
        '''Cancel any action from the FileChooserController.
        '''
        ...
    
    def on_touch_down(self, touch): # -> Literal[True] | None:
        ...
    
    def on_touch_move(self, touch): # -> Literal[True] | None:
        ...
    
    def on_touch_up(self, touch): # -> Literal[True] | None:
        ...
    


class FileChooserProgress(FileChooserProgressBase):
    ...


class FileChooserLayout(FloatLayout):
    '''Base class for file chooser layouts.

    .. versionadded:: 1.9.0
    '''
    VIEWNAME = ...
    __events__ = ...
    controller = ...
    def on_entry_added(self, node, parent=...): # -> None:
        ...
    
    def on_entries_cleared(self): # -> None:
        ...
    
    def on_subentry_to_entry(self, subentry, entry): # -> None:
        ...
    
    def on_remove_subentry(self, subentry, entry): # -> None:
        ...
    
    def on_submit(self, selected, touch=...): # -> None:
        ...
    


class FileChooserListLayout(FileChooserLayout):
    '''File chooser layout using a list view.

    .. versionadded:: 1.9.0
    '''
    VIEWNAME = ...
    _ENTRY_TEMPLATE = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def scroll_to_top(self, *args): # -> None:
        ...
    


class FileChooserIconLayout(FileChooserLayout):
    '''File chooser layout using an icon view.

    .. versionadded:: 1.9.0
    '''
    VIEWNAME = ...
    _ENTRY_TEMPLATE = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def scroll_to_top(self, *args): # -> None:
        ...
    


class FileChooserController(RelativeLayout):
    '''Base for implementing a FileChooser. Don't use this class directly, but
    prefer using an implementation such as the :class:`FileChooser`,
    :class:`FileChooserListView` or :class:`FileChooserIconView`.

    :Events:
        `on_entry_added`: entry, parent
            Fired when a root-level entry is added to the file list. If you
            return True from this event, the entry is not added to FileChooser.
        `on_entries_cleared`
            Fired when the the entries list is cleared, usually when the
            root is refreshed.
        `on_subentry_to_entry`: entry, parent
            Fired when a sub-entry is added to an existing entry or
            when entries are removed from an entry e.g. when
            a node is closed.
        `on_submit`: selection, touch
            Fired when a file has been selected with a double-tap.
    '''
    _ENTRY_TEMPLATE = ...
    layout = ...
    path = ...
    filters = ...
    filter_dirs = ...
    sort_func = ...
    files = ...
    show_hidden = ...
    selection = ...
    multiselect = ...
    dirselect = ...
    rootpath = ...
    progress_cls = ...
    file_encodings = ...
    file_system = ...
    font_name = ...
    _update_files_ev = ...
    _create_files_entries_ev = ...
    __events__ = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def on_touch_down(self, touch): # -> Literal[True] | None:
        ...
    
    def on_touch_up(self, touch): # -> Literal[True] | None:
        ...
    
    def on_entry_added(self, node, parent=...): # -> None:
        ...
    
    def on_entries_cleared(self): # -> None:
        ...
    
    def on_subentry_to_entry(self, subentry, entry): # -> None:
        ...
    
    def on_remove_subentry(self, subentry, entry): # -> None:
        ...
    
    def on_submit(self, selected, touch=...): # -> None:
        ...
    
    def entry_touched(self, entry, touch): # -> Literal[False] | None:
        '''(internal) This method must be called by the template when an entry
        is touched by the user.
        '''
        ...
    
    def entry_released(self, entry, touch): # -> Literal[False] | None:
        '''(internal) This method must be called by the template when an entry
        is touched by the user.

        .. versionadded:: 1.1.0
        '''
        ...
    
    def open_entry(self, entry): # -> None:
        ...
    
    def get_nice_size(self, fn): # -> LiteralString | Literal['', '--'] | None:
        '''Pass the filepath. Returns the size in the best human readable
        format or '' if it is a directory (Don't recursively calculate size).
        '''
        ...
    
    def cancel(self, *largs): # -> None:
        '''Cancel any background action started by filechooser, such as loading
        a new directory.

        .. versionadded:: 1.2.0
        '''
        ...
    
    def entry_subselect(self, entry): # -> None:
        ...
    
    def close_subselection(self, entry): # -> None:
        ...
    


class FileChooserListView(FileChooserController):
    '''Implementation of a :class:`FileChooserController` using a list view.

    .. versionadded:: 1.9.0
    '''
    _ENTRY_TEMPLATE = ...


class FileChooserIconView(FileChooserController):
    '''Implementation of a :class:`FileChooserController` using an icon view.

    .. versionadded:: 1.9.0
    '''
    _ENTRY_TEMPLATE = ...


class FileChooser(FileChooserController):
    '''Implementation of a :class:`FileChooserController` which supports
    switching between multiple, synced layout views.

    The FileChooser can be used as follows:

    .. code-block:: kv

        BoxLayout:
            orientation: 'vertical'

            BoxLayout:
                size_hint_y: None
                height: sp(52)

                Button:
                    text: 'Icon View'
                    on_press: fc.view_mode = 'icon'
                Button:
                    text: 'List View'
                    on_press: fc.view_mode = 'list'

            FileChooser:
                id: fc
                FileChooserIconLayout
                FileChooserListLayout

    .. versionadded:: 1.9.0
    '''
    manager = ...
    _view_list = ...
    def get_view_list(self): # -> List[Any]:
        ...
    
    view_list = ...
    _view_mode = ...
    def get_view_mode(self): # -> str:
        ...
    
    def set_view_mode(self, mode): # -> None:
        ...
    
    view_mode = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def add_widget(self, widget, *args, **kwargs): # -> None:
        ...
    
    def rebuild_views(self): # -> None:
        ...
    
    def update_view(self, *args): # -> None:
        ...
    
    def on_entry_added(self, node, parent=...): # -> None:
        ...
    
    def on_entries_cleared(self): # -> None:
        ...
    
    def on_subentry_to_entry(self, subentry, entry): # -> None:
        ...
    
    def on_remove_subentry(self, subentry, entry): # -> None:
        ...
    
    def on_submit(self, selected, touch=...): # -> None:
        ...
    


if __name__ == '__main__':
    root = ...
    class FileChooserApp(App):
        def build(self): # -> _ | Any | None:
            ...
        
    
    
