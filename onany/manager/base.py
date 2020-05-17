from typing import Dict, List


class EventManager:

    def __init__(self):
        self._events_pool: Dict[str, List[callable]] = {}

    def clear(self):
        self._events_pool = {}

    def listen(self, event: str, callback: callable):
        self._register_event(event)
        self._events_pool[event].append(callback)

    def emit(self, event: str, *args, **kwargs):
        self._register_event(event)

        for callback in self._events_pool[event]:
            callback(*args, **kwargs)

    def _register_event(self, event: str):
        if event not in self._events_pool:
            self._events_pool[event] = []
