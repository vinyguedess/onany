from typing import Dict, List


class OnAny:
    _events_pool: Dict[str, List[callable]] = {}

    @classmethod
    def listen(cls, event: str, callback: callable):
        cls._register_event(event)
        cls._events_pool[event].append(callback)

    @classmethod
    def emit(cls, event: str, *args, **kwargs):
        cls._register_event(event)

        for callback in cls._events_pool[event]:
            callback(*args, **kwargs)

    @classmethod
    def _register_event(cls, event: str):
        if event not in cls._events_pool:
            cls._events_pool[event] = []
