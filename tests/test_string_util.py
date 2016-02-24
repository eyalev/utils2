import unittest

from utils2.input_util import InputUtil
from utils2.string_util import StringUtil


class TestStringUtil(unittest.TestCase):

    def test_is_empty(self):

        self.assertEqual(StringUtil(None).is_empty(), True)
        self.assertEqual(StringUtil('').is_empty(), True)
        self.assertEqual(StringUtil(' ').is_empty(), True)
        self.assertEqual(StringUtil('\n\t   ').is_empty(), True)

        self.assertEqual(StringUtil('a').is_empty(), False)
        self.assertEqual(StringUtil('some_text').is_empty(), False)

    def test_is_valid_json(self):

        self.assertEqual(StringUtil('{"key": "value"}').is_valid_json(), True)
        self.assertEqual(StringUtil('{}').is_valid_json(), True)

        self.assertEqual(StringUtil(None).is_valid_json(), False)
        self.assertEqual(StringUtil('').is_valid_json(), False)
        self.assertEqual(StringUtil('some_text').is_valid_json(), False)

    def test_to_datetime(self):

        datetime_strings = [
            '2016-02-24T01:00:00',
            '2016-02-24T01:00:00Z',
            '2016-02-24T01:00:00.123456',
            '2016-02-24T01:00:00.123456Z',
        ]

        for datetime_string in datetime_strings:
            _datetime = StringUtil(datetime_string).to_datetime()
            self.assertTrue(InputUtil(_datetime).is_datetime())
