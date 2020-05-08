========================
OnAny... thing happening
========================

.. image:: https://github.com/vinyguedess/onany/workflows/OnAny%20CI%20Test/badge.svg
    :target: https://github.com/vinyguedess/onany/actions?query=workflow%3A%22OnAny+CI+Test%22
    :alt: Build

.. image:: https://api.codeclimate.com/v1/badges/c9f11d97d33668424612/maintainability
   :target: https://codeclimate.com/github/vinyguedess/onany/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/c9f11d97d33668424612/test_coverage
   :target: https://codeclimate.com/github/vinyguedess/onany/test_coverage
   :alt: Test Coverage


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

Webhook listener
================
It's possible declare webhook rules to be dispatched as an inside event.
This webhook events can be a powerful tool for communicating to third-party
clients that an event is ended.

**Listener rules**:

- **route**
    - **type**: str
    - **description**: API route
    - **required**
- **callback**
    - **type**: callable/function
    - **description**: Receives request response object if needed

When **dispatch** or **disthread** is called is possible define some attributes to
be sent in the external API call.

**Attributes**:

- **data**
    - **type**: dict
    - **description**: JSON body
- **headers**
    - **type**: dict
    - **description**: Dictionary declaring headers to be sent

**Example**:

.. code :: python

    from onany import dispatch, listener

    def event_name_webhook_response(response):
        if response.status_code == 200:
            print("My hook listener worked")

    listener("event.name", {
        "route": "https://my.api/hooks",
        "callback": event_name_webhook_response
    })

    >>> dispatch("event.name", data={
        "some": "payload",
        "I": "wanna",
        "send": "to",
        "hooked": "api"
    })
