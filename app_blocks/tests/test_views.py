from django.urls import reverse
from django.test import TestCase
from app_blocks.models import Block


DEFAULT_BLOCKS = [
    {
        'height': '230605',
        'hash': '66e0a15db61cddec3bda9318a7d8e32352b5f6fa24b3b37fee70f14f6a9b8ff5',
        'timestamp': '1612356672',
        'miner': 'BTJi34JG4dmL5GbTYgDdp8Nyb7Mhpsd1az',
        'transactions_count': '2'
    },
    {
        'height': '230604',
        'hash': '266b79ed796301afcd81114f4590e6d326acc808a42ca0ab5fc59fd4858e650d',
        'timestamp': '1612356624',
        'miner': 'BTJi34JG4dmL5GbTYgDdp8Nyb7Mhpsd1az',
        'transactions_count': '2'
    },
    {
        'height': '230603',
        'hash': '20563330b85010599dff75f6612bf6d8e7b133e53381f644301ceb680c6ff3fd',
        'timestamp': '1612356288',
        'miner': 'BTJi34JG4dmL5GbTYgDdp8Nyb7Mhpsd1az',
        'transactions_count': '2'
    },
]


class BlocksTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for block_info in DEFAULT_BLOCKS:
            Block.objects.create(
                height=block_info['height'],
                hash=block_info['hash'],
                timestamp=block_info['timestamp'],
                miner=block_info['miner'],
                transactions_count=block_info['transactions_count'],
            )

    def test_all_blogs_exist_at_desired_location(self):
        url = reverse('all_blocks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blocks/all_blocks.html')

    def test_blocks_number(self):
        url = reverse('all_blocks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['blocks']) <= 50)

    def test_block_info_exist_at_desired_location(self):
        block = Block.objects.all().first()
        response = self.client.get(f'/blocks/{block.height}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blocks/block_detail.html')
