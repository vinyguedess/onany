import os
from typing import Any, Dict
from unittest import TestCase
from dotenv import load_dotenv
from tests.generators import sprint, get_last_sprint
from onany import clear_listeners, dispatch, disthread, get_manager, listener, set_manager


class TestOnAny(TestCase):

    def setUp(self):
        self.called = False

        load_dotenv()
        clear_listeners()

    def test_dispatch_listen(self):
        set_manager(
            "rabbitmq",
            host=os.getenv("AMQP_HOST"),
            user=os.getenv("AMQP_USER"),
            password=os.getenv("AMQP_PASS"),
            vhost=os.getenv("AMQP_USER"))

        callback = self.get_listener()
        dispatch("listening", hello="world")

        self.assertTrue(self.called)

    def get_listener(self, event: str = "listening"):
        
        @listener(event)
        def callback(*args, **kwargs):
            self.called = True

        return callback
