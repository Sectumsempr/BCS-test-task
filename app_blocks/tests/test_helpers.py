from django.test import TestCase
from app_blocks.helpers import get_blocks, get_block


class ApiGettersTest(TestCase):
    def test_get_blocks_returns_list(self):
        blocks = get_blocks()
        self.assertEqual(type(blocks), list)

    def test_get_block_returns_false(self):
        block = get_block('!9304!')
        self.assertFalse(block)

    def test_get_block_returns_dict(self):
        block = get_block('22')
        self.assertEqual(type(block), dict)
