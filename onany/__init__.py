from threading import Thread
from typing import Any, Dict, Union
from onany.manager import EventManager
from onany.web import webhook_callback


def clear_listeners():
    EventManager.clear()


def dispatch(event: str, *args, **kwargs) -> None:
    return EventManager.emit(event, *args, **kwargs)


def disthread(event: str, *args, **kwargs) -> Thread:
    thread: Thread = Thread(
        target=EventManager.emit,
        args=(event, *args,),
        kwargs=kwargs)
    thread.start()

    return thread


def listener(event: str, callback: Union[callable, Dict[str, Any]] = None) -> callable:
    if callable(callback):
        return EventManager.listen(event, callback)

    if callback and isinstance(callback, dict):
        return EventManager.listen(
            event, 
            webhook_callback(callback))

    def wrapper(callback: callable) -> None:
        return EventManager.listen(event, callback)

    return wrapper
