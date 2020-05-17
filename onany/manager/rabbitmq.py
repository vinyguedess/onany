import json
from threading import Thread
import pika
from onany.manager.base import EventManager


class RabbitMQManager(EventManager):

    def __init__(self, **kwargs):
        super(RabbitMQManager, self).__init__()

        self.channel = kwargs.get("channel", "onany")
        self._conn = self._get_connection(
            kwargs.get("host"),
            kwargs.get("user"),
            kwargs.get("password"),
            vhost=kwargs.get("vhost"))

    def emit(self, event: str, *args, **kwargs):
        channel = self._conn.channel()
        channel.basic_publish(
            exchange="",
            routing_key=self.channel,
            body=json.dumps({
                "event": event,
                "args": args,
                "kwargs": kwargs
            }))

        self._on_message_received(channel)

    def _on_message_received(self, channel):
        
        while True:
            method, properties, body = channel.basic_get(self.channel)
            if not method:
                break

            payload = json.loads(body)
            super(RabbitMQManager, self).emit(
                payload.get("event"),
                *payload.get("args"),
                **payload.get("kwargs"))

            channel.basic_ack(method.delivery_tag)

    def _get_connection(self, host: str, user: str, password: str, **kwargs):
        credentials = pika.PlainCredentials(user, password)

        parameters = pika.ConnectionParameters(
            host=host,
            credentials=credentials,
            virtual_host=kwargs.get("vhost"))

        return pika.BlockingConnection(parameters)
