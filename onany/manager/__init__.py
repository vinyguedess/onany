from onany.manager.memory import MemoryManager
from onany.manager.rabbitmq import RabbitMQManager


def event_manager_factory(manager: str, **kwargs):
    if manager == "memory":
        return MemoryManager(**kwargs)
    elif manager == "rabbitmq":
        return RabbitMQManager(**kwargs)

    return None
