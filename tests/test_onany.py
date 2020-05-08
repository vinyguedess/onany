from typing import Any, Dict
from unittest import TestCase
from tests.generators import sprint, get_last_sprint
from onany import clear_listeners, dispatch, disthread, listener


class TestOnAny(TestCase):

    def setUp(self):
        clear_listeners()

    def test_dispatch_listen(self):
        callback = self.get_listener()
        params = {
            "called_once": False
        }

        dispatch("listening", params=params)

        self.assertTrue(params.get("called_once"))

    def test_dispatch_listen_registering_simple_callback(self):
        listener(
            "event.name", 
            lambda name: 
                sprint("Hello {}. Welcome to OnAny!".format(name)))

        dispatch("event.name", "Clark Kent")

        self.assertEqual(get_last_sprint(), "Hello Clark Kent. Welcome to OnAny!")

    def test_dispatch_listen_webhook_callback(self):
        listener("event.name", {
            "route": "http://demo2158329.mockable.io/callback",
            "callback": lambda response: 
                sprint("API Answered with {}".format(response.status_code))
        })

        dispatch("event.name", data={
            "name": "Bruce Wayne"
        })

        self.assertEqual(get_last_sprint(), "API Answered with 200")

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
