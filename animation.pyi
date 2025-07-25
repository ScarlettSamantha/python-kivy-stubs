"""
This type stub file was generated by pyright.
"""

from kivy.event import EventDispatcher

'''
Animation
=========

:class:`Animation` and :class:`AnimationTransition` are used to animate
:class:`~kivy.uix.widget.Widget` properties. You must specify at least a
property name and target value. To use an Animation, follow these steps:

    * Setup an Animation object
    * Use the Animation object on a Widget

Simple animation
----------------

To animate a Widget's x or y position, simply specify the target x/y values
where you want the widget positioned at the end of the animation::

    anim = Animation(x=100, y=100)
    anim.start(widget)

The animation will last for 1 second unless :attr:`duration` is specified.
When anim.start() is called, the Widget will move smoothly from the current
x/y position to (100, 100).

Multiple properties and transitions
-----------------------------------

You can animate multiple properties and use built-in or custom transition
functions using :attr:`transition` (or the `t=` shortcut). For example,
to animate the position and size using the 'in_quad' transition::

    anim = Animation(x=50, size=(80, 80), t='in_quad')
    anim.start(widget)

Note that the `t=` parameter can be the string name of a method in the
:class:`AnimationTransition` class or your own animation function.

Sequential animation
--------------------

To join animations sequentially, use the '+' operator. The following example
will animate to x=50 over 1 second, then animate the size to (80, 80) over the
next two seconds::

    anim = Animation(x=50) + Animation(size=(80, 80), duration=2.)
    anim.start(widget)

Parallel animation
------------------

To join animations in parallel, use the '&' operator. The following example
will animate the position to (80, 10) over 1 second, whilst in parallel
animating the size to (800, 800)::

    anim = Animation(pos=(80, 10))
    anim &= Animation(size=(800, 800), duration=2.)
    anim.start(widget)

Keep in mind that creating overlapping animations on the same property may have
unexpected results. If you want to apply multiple animations to the same
property, you should either schedule them sequentially (via the '+' operator or
using the *on_complete* callback) or cancel previous animations using the
:attr:`~Animation.cancel_all` method.

Repeating animation
-------------------

.. versionadded:: 1.8.0

.. note::
    This is currently only implemented for 'Sequence' animations.

To set an animation to repeat, simply set the :attr:`Sequence.repeat`
property to `True`::

    anim = Animation(...) + Animation(...)
    anim.repeat = True
    anim.start(widget)

For flow control of animations such as stopping and cancelling, use the methods
already in place in the animation module.
'''
__all__ = ('Animation', 'AnimationTransition')
class Animation(EventDispatcher):
    '''Create an animation definition that can be used to animate a Widget.

    :Parameters:
        `duration` or `d`: float, defaults to 1.
            Duration of the animation, in seconds.
        `transition` or `t`: str or func
            Transition function for animate properties. It can be the name of a
            method from :class:`AnimationTransition`.
        `step` or `s`: float
            Step in milliseconds of the animation. Defaults to 0, which means
            the animation is updated for every frame.

            To update the animation less often, set the step value to a float.
            For example, if you want to animate at 30 FPS, use s=1/30.

    :Events:
        `on_start`: animation, widget
            Fired when the animation is started on a widget.
        `on_complete`: animation, widget
            Fired when the animation is completed or stopped on a widget.
        `on_progress`: animation, widget, progression
            Fired when the progression of the animation is changing.

    .. versionchanged:: 1.4.0
        Added s/step parameter.

    .. versionchanged:: 1.10.0
        The default value of the step parameter was changed from 1/60. to 0.
    '''
    _update_ev = ...
    _instances = ...
    __events__ = ...
    def __init__(self, **kw) -> None:
        ...
    
    @property
    def duration(self):
        '''Return the duration of the animation.
        '''
        ...
    
    @property
    def transition(self): # -> Any:
        '''Return the transition of the animation.
        '''
        ...
    
    @property
    def animated_properties(self): # -> dict[str, Any]:
        '''Return the properties used to animate.
        '''
        ...
    
    @staticmethod
    def stop_all(widget, *largs): # -> None:
        '''Stop all animations that concern a specific widget / list of
        properties.

        Example::

            anim = Animation(x=50)
            anim.start(widget)

            # and later
            Animation.stop_all(widget, 'x')
        '''
        ...
    
    @staticmethod
    def cancel_all(widget, *largs): # -> None:
        '''Cancel all animations that concern a specific widget / list of
        properties. See :attr:`cancel`.

        Example::

            anim = Animation(x=50)
            anim.start(widget)

            # and later
            Animation.cancel_all(widget, 'x')

        .. versionadded:: 1.4.0

        .. versionchanged:: 2.1.0
            If the parameter ``widget`` is None, all animated widgets will be
            the target and cancelled. If ``largs`` is also given, animation of
            these properties will be canceled for all animated widgets.
        '''
        ...
    
    def start(self, widget): # -> None:
        '''Start the animation on a widget.
        '''
        ...
    
    def stop(self, widget): # -> None:
        '''Stop the animation previously applied to a widget, triggering the
        `on_complete` event.'''
        ...
    
    def cancel(self, widget): # -> None:
        '''Cancel the animation previously applied to a widget. Same
        effect as :attr:`stop`, except the `on_complete` event will
        *not* be triggered!

        .. versionadded:: 1.4.0
        '''
        ...
    
    def stop_property(self, widget, prop): # -> None:
        '''Even if an animation is running, remove a property. It will not be
        animated further. If it was the only/last property being animated,
        the animation will be stopped (see :attr:`stop`).
        '''
        ...
    
    def cancel_property(self, widget, prop): # -> None:
        '''Even if an animation is running, remove a property. It will not be
        animated further. If it was the only/last property being animated,
        the animation will be canceled (see :attr:`cancel`)

        .. versionadded:: 1.4.0
        '''
        ...
    
    def have_properties_to_animate(self, widget): # -> Literal[True] | None:
        '''Return True if a widget still has properties to animate.

        .. versionadded:: 1.8.0
        '''
        ...
    
    def on_start(self, widget): # -> None:
        ...
    
    def on_progress(self, widget, progress): # -> None:
        ...
    
    def on_complete(self, widget): # -> None:
        ...
    
    def __add__(self, animation): # -> Sequence:
        ...
    
    def __and__(self, animation): # -> Parallel:
        ...
    


class CompoundAnimation(Animation):
    def stop_property(self, widget, prop): # -> None:
        ...
    
    def cancel(self, widget): # -> None:
        ...
    
    def cancel_property(self, widget, prop): # -> None:
        '''Even if an animation is running, remove a property. It will not be
        animated further. If it was the only/last property being animated,
        the animation will be canceled (see :attr:`cancel`)

        This method overrides `:class:kivy.animation.Animation`'s
        version, to cancel it on all animations of the Sequence.

        .. versionadded:: 1.10.0
        '''
        ...
    
    def have_properties_to_animate(self, widget):
        ...
    
    @property
    def animated_properties(self): # -> ChainMap[Any, Any]:
        ...
    
    @property
    def transition(self):
        ...
    


class Sequence(CompoundAnimation):
    def __init__(self, anim1, anim2) -> None:
        ...
    
    @property
    def duration(self):
        ...
    
    def stop(self, widget): # -> None:
        ...
    
    def start(self, widget): # -> None:
        ...
    
    def on_anim1_complete(self, instance, widget): # -> None:
        ...
    
    def on_anim1_progress(self, instance, widget, progress): # -> None:
        ...
    
    def on_anim2_complete(self, instance, widget): # -> None:
        '''Repeating logic used with boolean variable "repeat".

        .. versionadded:: 1.7.1
        '''
        ...
    
    def on_anim2_progress(self, instance, widget, progress): # -> None:
        ...
    


class Parallel(CompoundAnimation):
    def __init__(self, anim1, anim2) -> None:
        ...
    
    @property
    def duration(self):
        ...
    
    def stop(self, widget): # -> None:
        ...
    
    def start(self, widget): # -> None:
        ...
    
    def on_anim_complete(self, instance, widget): # -> None:
        ...
    


class AnimationTransition:
    '''Collection of animation functions to be used with the Animation object.
    Easing Functions ported to Kivy from the Clutter Project
    https://developer.gnome.org/clutter/stable/ClutterAlpha.html

    The `progress` parameter in each animation function is in the range 0-1.
    '''
    @staticmethod
    def linear(progress):
        '''.. image:: images/anim_linear.png'''
        ...
    
    @staticmethod
    def in_quad(progress):
        '''.. image:: images/anim_in_quad.png
        '''
        ...
    
    @staticmethod
    def out_quad(progress):
        '''.. image:: images/anim_out_quad.png
        '''
        ...
    
    @staticmethod
    def in_out_quad(progress):
        '''.. image:: images/anim_in_out_quad.png
        '''
        ...
    
    @staticmethod
    def in_cubic(progress):
        '''.. image:: images/anim_in_cubic.png
        '''
        ...
    
    @staticmethod
    def out_cubic(progress):
        '''.. image:: images/anim_out_cubic.png
        '''
        ...
    
    @staticmethod
    def in_out_cubic(progress):
        '''.. image:: images/anim_in_out_cubic.png
        '''
        ...
    
    @staticmethod
    def in_quart(progress):
        '''.. image:: images/anim_in_quart.png
        '''
        ...
    
    @staticmethod
    def out_quart(progress):
        '''.. image:: images/anim_out_quart.png
        '''
        ...
    
    @staticmethod
    def in_out_quart(progress):
        '''.. image:: images/anim_in_out_quart.png
        '''
        ...
    
    @staticmethod
    def in_quint(progress):
        '''.. image:: images/anim_in_quint.png
        '''
        ...
    
    @staticmethod
    def out_quint(progress):
        '''.. image:: images/anim_out_quint.png
        '''
        ...
    
    @staticmethod
    def in_out_quint(progress):
        '''.. image:: images/anim_in_out_quint.png
        '''
        ...
    
    @staticmethod
    def in_sine(progress): # -> float:
        '''.. image:: images/anim_in_sine.png
        '''
        ...
    
    @staticmethod
    def out_sine(progress): # -> float:
        '''.. image:: images/anim_out_sine.png
        '''
        ...
    
    @staticmethod
    def in_out_sine(progress): # -> float:
        '''.. image:: images/anim_in_out_sine.png
        '''
        ...
    
    @staticmethod
    def in_expo(progress): # -> float:
        '''.. image:: images/anim_in_expo.png
        '''
        ...
    
    @staticmethod
    def out_expo(progress): # -> float:
        '''.. image:: images/anim_out_expo.png
        '''
        ...
    
    @staticmethod
    def in_out_expo(progress): # -> float:
        '''.. image:: images/anim_in_out_expo.png
        '''
        ...
    
    @staticmethod
    def in_circ(progress): # -> float:
        '''.. image:: images/anim_in_circ.png
        '''
        ...
    
    @staticmethod
    def out_circ(progress): # -> float:
        '''.. image:: images/anim_out_circ.png
        '''
        ...
    
    @staticmethod
    def in_out_circ(progress): # -> float:
        '''.. image:: images/anim_in_out_circ.png
        '''
        ...
    
    @staticmethod
    def in_elastic(progress): # -> float:
        '''.. image:: images/anim_in_elastic.png
        '''
        ...
    
    @staticmethod
    def out_elastic(progress): # -> float:
        '''.. image:: images/anim_out_elastic.png
        '''
        ...
    
    @staticmethod
    def in_out_elastic(progress): # -> float:
        '''.. image:: images/anim_in_out_elastic.png
        '''
        ...
    
    @staticmethod
    def in_back(progress):
        '''.. image:: images/anim_in_back.png
        '''
        ...
    
    @staticmethod
    def out_back(progress):
        '''.. image:: images/anim_out_back.png
        '''
        ...
    
    @staticmethod
    def in_out_back(progress):
        '''.. image:: images/anim_in_out_back.png
        '''
        ...
    
    @staticmethod
    def in_bounce(progress):
        '''.. image:: images/anim_in_bounce.png
        '''
        ...
    
    @staticmethod
    def out_bounce(progress):
        '''.. image:: images/anim_out_bounce.png
        '''
        ...
    
    @staticmethod
    def in_out_bounce(progress):
        '''.. image:: images/anim_in_out_bounce.png
        '''
        ...
    


