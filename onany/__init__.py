from threading import Thread
from onany.manager import OnAny


def dispatch(event: str, *args, **kwargs) -> None:
    return OnAny.emit(event, *args, **kwargs)


def disthread(event: str, *args, **kwargs) -> Thread:
    thread: Thread = Thread(
        target=OnAny.emit,
        args=(event, *args,),
        kwargs=kwargs)
    thread.start()

    return thread


def listener(event: str) -> callable:
    def wrapper(callback: callable) -> None:
        return OnAny.listen(event, callback)

    return wrapper
