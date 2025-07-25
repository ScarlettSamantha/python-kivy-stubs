"""
This type stub file was generated by pyright.
"""

'''
.. _motionevent:

Motion Event
============

The :class:`MotionEvent` is the base class used for events provided by
pointing devices (touch and non-touch). This class defines all the properties
and methods needed to handle 2D and 3D movements but has many more
capabilities.

Usually you would never need to create the :class:`MotionEvent` yourself as
this is the role of the :mod:`~kivy.input.providers`.

Flow of the motion events
-------------------------

1. The :class:`MotionEvent` 's are gathered from input providers by
   :class:`~kivy.base.EventLoopBase`.
2. Post processing is performed by registered processors
   :mod:`~kivy.input.postproc`.
3. :class:`~kivy.base.EventLoopBase` dispatches all motion events using
   `on_motion` event to all registered listeners including the
   :class:`~kivy.core.window.WindowBase`.
4. Once received in :meth:`~kivy.core.window.WindowBase.on_motion` events
   (touch or non-touch) are all registered managers. If a touch event is not
   handled by at least one manager, then it is dispatched through
   :meth:`~kivy.core.window.WindowBase.on_touch_down`,
   :meth:`~kivy.core.window.WindowBase.on_touch_move` and
   :meth:`~kivy.core.window.WindowBase.on_touch_up`.
5. Widgets receive events in :meth:`~kivy.uix.widget.Widget.on_motion` method
   (if passed by a manager) or on `on_touch_xxx` methods.

Motion events and event managers
--------------------------------

A motion event is a touch event if its :attr:`MotionEvent.is_touch` is set to
`True`. Beside `is_touch` attribute, :attr:`MotionEvent.type_id` can be used to
check for event's general type. Currently two types are dispatched by
input providers: "touch" and "hover".

Event managers can be used to dispatch any motion event throughout the widget
tree and a manager uses `type_id` to specify which event types it want to
receive. See :mod:`~kivy.eventmanager` to learn how to define and register
an event manager.

A manager can also assign a new `type_id` to
:attr:`MotionEvent.type_id` before dispatching it to the widgets. This useful
when dispatching a specific event::

    class MouseTouchManager(EventManagerBase):

        type_ids = ('touch',)

        def dispatch(self, etype, me):
            accepted = False
            if me.device == 'mouse':
                me.push() # Save current type_id and other values
                me.type_id = 'mouse_touch'
                self.window.transform_motion_event_2d(me)
                # Dispatch mouse touch event to widgets which registered
                # to receive 'mouse_touch'
                for widget in self.window.children[:]:
                    if widget.dispatch('on_motion', etype, me):
                        accepted = True
                        break
                me.pop() # Restore
            return accepted

Listening to a motion event
---------------------------

If you want to receive all motion events, touch or not, you can bind the
MotionEvent from the :class:`~kivy.core.window.Window` to your own callback::

    def on_motion(self, etype, me):
        # will receive all motion events.
        pass

    Window.bind(on_motion=on_motion)

You can also listen to changes of the mouse position by watching
:attr:`~kivy.core.window.WindowBase.mouse_pos`.

Profiles
--------

The :class:`MotionEvent` stores device specific information in various
properties listed in the :attr:`~MotionEvent.profile`.
For example, you can receive a MotionEvent that has an angle, a fiducial
ID, or even a shape. You can check the :attr:`~MotionEvent.profile`
attribute to see what is currently supported by the MotionEvent provider.

This is a short list of the profile values supported by default. Please check
the :attr:`MotionEvent.profile` property to see what profile values are
available.

============== ================================================================
Profile value   Description
-------------- ----------------------------------------------------------------
angle          2D angle. Accessed via the `a` property.
button         Mouse button ('left', 'right', 'middle', 'scrollup' or
               'scrolldown'). Accessed via the `button` property.
markerid       Marker or Fiducial ID. Accessed via the `fid` property.
pos            2D position. Accessed via the `x`, `y` or `pos` properties.
pos3d          3D position. Accessed via the `x`, `y` or `z` properties.
pressure       Pressure of the contact. Accessed via the `pressure` property.
shape          Contact shape. Accessed via the `shape` property .
============== ================================================================

If you want to know whether the current :class:`MotionEvent` has an angle::

    def on_touch_move(self, touch):
        if 'angle' in touch.profile:
            print('The touch angle is', touch.a)

If you want to select only the fiducials::

    def on_touch_move(self, touch):
        if 'markerid' not in touch.profile:
            return

'''
__all__ = ('MotionEvent', )
class EnhancedDictionary(dict):
    def __getattr__(self, attr):
        ...
    
    def __setattr__(self, attr, value): # -> None:
        ...
    


class MotionEventMetaclass(type):
    def __new__(mcs, name, bases, attrs): # -> Self:
        ...
    


MotionEventBase = ...
class MotionEvent(MotionEventBase):
    '''Abstract class that represents an input event.

    :Parameters:
        `id`: str
            unique ID of the MotionEvent
        `args`: list
            list of parameters, passed to the depack() function
    '''
    __uniq_id = ...
    __attrs__ = ...
    def __init__(self, device, id, args, is_touch=..., type_id=...) -> None:
        ...
    
    def depack(self, args): # -> None:
        '''Depack `args` into attributes of the class'''
        ...
    
    def grab(self, class_instance, exclusive=...): # -> None:
        '''Grab this motion event.

        If this event is a touch you can grab it if you want to receive
        subsequent :meth:`~kivy.uix.widget.Widget.on_touch_move` and
        :meth:`~kivy.uix.widget.Widget.on_touch_up` events, even if the touch
        is not dispatched by the parent:

        .. code-block:: python

            def on_touch_down(self, touch):
                touch.grab(self)

            def on_touch_move(self, touch):
                if touch.grab_current is self:
                    # I received my grabbed touch
                else:
                    # it's a normal touch

            def on_touch_up(self, touch):
                if touch.grab_current is self:
                    # I receive my grabbed touch, I must ungrab it!
                    touch.ungrab(self)
                else:
                    # it's a normal touch
                    pass

        .. versionchanged:: 2.1.0
            Allowed grab for non-touch events.
        '''
        ...
    
    def ungrab(self, class_instance): # -> None:
        '''Ungrab a previously grabbed motion event.
        '''
        ...
    
    def dispatch_done(self): # -> None:
        '''Notify that dispatch to the listeners is done.

        Called by the :meth:`EventLoopBase.post_dispatch_input`.

        .. versionadded:: 2.1.0
        '''
        ...
    
    def move(self, args): # -> None:
        '''Move to another position.
        '''
        ...
    
    def scale_for_screen(self, w, h, p=..., rotation=..., smode=..., kheight=...): # -> None:
        '''Scale position for the screen.

        .. versionchanged:: 2.1.0
            Max value for `x`, `y` and `z` is changed respectively to `w` - 1,
            `h` - 1 and `p` - 1.
        '''
        ...
    
    def to_absolute_pos(self, nx, ny, x_max, y_max, rotation): # -> tuple[Any, Any]:
        '''Transforms normalized (0-1) coordinates `nx` and `ny` to absolute
        coordinates using `x_max`, `y_max` and `rotation`.

        :raises:
            `ValueError`: If `rotation` is not one of: 0, 90, 180 or 270

        .. versionadded:: 2.1.0
        '''
        ...
    
    def push(self, attrs=...): # -> None:
        '''Push attribute values in `attrs` onto the stack.
        '''
        ...
    
    def pop(self): # -> None:
        '''Pop attributes values from the stack.
        '''
        ...
    
    def apply_transform_2d(self, transform): # -> None:
        '''Apply a transformation on x, y, z, px, py, pz,
        ox, oy, oz, dx, dy, dz.
        '''
        ...
    
    def copy_to(self, to): # -> None:
        '''Copy some attribute to another motion event object.'''
        ...
    
    def distance(self, other_touch): # -> float:
        '''Return the distance between the two events.
        '''
        ...
    
    def update_time_end(self): # -> None:
        ...
    
    @property
    def dpos(self): # -> tuple[Any | None, Any | None]:
        '''Return delta between last position and current position, in the
        screen coordinate system (self.dx, self.dy).'''
        ...
    
    @property
    def opos(self): # -> tuple[Any | None, Any | None]:
        '''Return the initial position of the motion event in the screen
        coordinate system (self.ox, self.oy).'''
        ...
    
    @property
    def ppos(self): # -> tuple[Any | None, Any | None]:
        '''Return the previous position of the motion event in the screen
        coordinate system (self.px, self.py).'''
        ...
    
    @property
    def spos(self): # -> tuple[float, float]:
        '''Return the position in the 0-1 coordinate system (self.sx, self.sy).
        '''
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def is_mouse_scrolling(self, *args): # -> bool:
        '''Returns True if the touch event is a mousewheel scrolling

        .. versionadded:: 1.6.0
        '''
        ...
    


