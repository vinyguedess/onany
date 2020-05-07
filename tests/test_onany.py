from typing import Any, Dict
from unittest import TestCase
from onany import dispatch, disthread, listener


class TestOnAny(TestCase):

    def test_dispatch_listen(self):
        callback = self.get_listener()
        params = {
            "called_once": False
        }

        dispatch("listening", params=params)

        self.assertTrue(params.get("called_once"))

    def test_thread_dispatch_listen(self):
        callback = self.get_listener()
        params = {
            "called_once": False
        }

        thread = disthread("listening", params=params)
        thread.join()

        self.assertTrue(params.get("called_once"))

    def get_listener(self, event: str = "listening"):
        
        @listener(event)
        def callback(params: Dict[str, Any]):
            params.update({
                "called_once": True
            })

        return callback
