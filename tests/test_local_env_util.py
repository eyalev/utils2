import unittest
from utils2.file_util import FileUtil
from utils2.dict_util import odict, DictUtil
from utils2.local_env_util import LocalEnvUtil


class TestLocalEnvUtil(unittest.TestCase):

    def test_local_env_util(self):

        env_file_path = 'tests/tmp/env.json'
        env_file_contents = DictUtil(odict([
            ('key', 'value')
        ])).to_json_string()

        FileUtil(env_file_path).write(env_file_contents)

        value = LocalEnvUtil(env_file_path='tests/tmp/env.json').get('key')
        self.assertEqual(value, 'value')
