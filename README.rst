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

Should I wait all callbacks to end ?
====================================
Nope. You can "threadily" dispatch your events so they 
don't need to be waited for the main process.

.. code :: python

    from onany import disthread, listener

    @listener("event.name")
    def on_event_name():
        print("I'm gonna be executed on another thread")

    >>> disthread("event.name")
