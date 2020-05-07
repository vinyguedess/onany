========================
OnAny... thing happening
========================

OnAny is a simple yet powerful event manager library, where you can declare listeners and dispatch as much events as needed to them.

How To
======
To listen and dispatch events is very simple:

.. code :: python
    
    from onany import dispatch, listener

    @listener("event.name")
    def on_event_name(*args, **kwargs):
        print("I've been called with {} and {}".format(
            args,
            kwargs
        ))

    >>> dispatch(
        "event.name",
        "first_param",
        "second_param",
        "third_param",
        first="param",
        second="param",
        third="param")
