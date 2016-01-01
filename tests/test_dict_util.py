import unittest
from utils2.dict_util import DictUtil


class TestDictUtil(unittest.TestCase):

    def test_to_json(self):

        _dict = {
            'key': 'value'
        }

        self.assertEqual(DictUtil(_dict).to_json_string(), '{"key": "value"}')
