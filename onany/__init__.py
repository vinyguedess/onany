from threading import Thread
from typing import Any, Dict, Union
from onany.manager import EventManager
from onany.web import webhook_callback


def clear_listeners():
    """Clear listeners registered"""

    EventManager.clear()


def dispatch(event: str, *args, **kwargs) -> None:
    """Dispatch an event to registered listeners.
    
    :param event: Event to be triggered
    :param *args: Optional args to be redirect to listeners
    :param **kwargs: Optional keyed args to be redirect to listeners
    """

    return EventManager.emit(event, *args, **kwargs)


def disthread(event: str, *args, **kwargs) -> Thread:
    """Through a thread dispatch an event to registered listeners.

    :param event: Event to be triggered
    :param *args: Optional args to be redirect to listeners
    :param **kwargs: Optional keyed args to be redirect to listeners
    """

    thread: Thread = Thread(
        target=EventManager.emit,
        args=(event, *args,),
        kwargs=kwargs)
    thread.start()

    return thread


def listener(event: str, callback: Union[callable, Dict[str, Any]] = None) -> callable:
    """Register a listener to be triggered by defined event on the future.
    
    There're two different types of listeners:
        1. Callable: The common one, listener is defined as a callable
        and can be triggered whenever desired.
        2. Hook: Listener is defined as a dictionary with rules indicating
        how an API andpoint can be called.

    Callable:
        Decorator:
            >>> from onany import dispatch, listener
            
            @listener("event.name")
            def on_event():
                print("Do something")

            >>> dispatch("event.name")

        Register:
            >>> from onany import dispatch, listener

            def on_event():
                print("Do something")

            >>> listener("event.name", on_event)
            >>> dispatch("event.name")

    Hook:
        >>> from onany import dispatch, listener

        def api_callback_if_i_need_to_know_response(response):
            if response.status_code !== 200:
                print("some thing happen'd")

        >>> listener("event.name", {
            "route": "https://my.api.io/hook",
            "callback": api_callback_if_i_need_to_know_response
        })

        >>> data = {
            "optional": "hook",
            "json": "payload"
        }

        >>> dispatch("event.name", data=data)

    :param event: Event to be listened
    :param callback: (Optional) can be a listener or rules to a hook dispatch
    """

    if callable(callback):
        return EventManager.listen(event, callback)

    if callback and isinstance(callback, dict):
        return EventManager.listen(
            event, 
            webhook_callback(callback))

    def wrapper(callback: callable) -> None:
        return EventManager.listen(event, callback)

    return wrapper
