import unittest

from unittest.mock import MagicMock
from utils2.file_util import FileUtil


class TestFileUtil(unittest.TestCase):

    def test_is_empty(self):

        file_util = FileUtil(None)

        file_util.data = MagicMock(return_value=None)
        self.assertEqual(file_util.is_empty(), True)

        file_util.data = MagicMock(return_value='')
        self.assertEqual(file_util.is_empty(), True)

        file_util.data = MagicMock(return_value='  \n\t')
        self.assertEqual(file_util.is_empty(), True)

        file_util.data = MagicMock(return_value='some_text')
        self.assertEqual(file_util.is_empty(), False)

    def test_is_valid_json(self):

        file_util = FileUtil(None)

        file_util.data = MagicMock(return_value='{"key": "value"}')
        self.assertEqual(file_util.is_valid_json(), True)

        file_util.data = MagicMock(return_value='{}')
        self.assertEqual(file_util.is_valid_json(), True)

        file_util.data = MagicMock(return_value=None)
        self.assertEqual(file_util.is_valid_json(), False)

        file_util.data = MagicMock(return_value='some_text')
        self.assertEqual(file_util.is_valid_json(), False)

        file_util.data = MagicMock(return_value='')
        self.assertEqual(file_util.is_valid_json(), False)
