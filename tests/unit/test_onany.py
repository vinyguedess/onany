from unittest import TestCase
from onany import get_manager, set_manager
from onany.manager.memory import MemoryManager


class TestOnAnySetManager(TestCase):

    def test_set_event_manager(self):
        set_manager("memory")
        
        self.assertIsInstance(get_manager(), MemoryManager)

    def test_set_event_manager_error_if_invalid_manager(self):
        set_manager("invalid")

        self.assertIsNone(get_manager())
