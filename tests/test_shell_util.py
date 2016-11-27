import unittest

from pathlib2 import Path

from utils2.shell_util import run_and_return_output, run


class TestShellUtil(unittest.TestCase):

    def test_run_and_return_output(self):

        output = run_and_return_output('echo -n test1')

        self.assertEqual(output, 'test1')

    def test_run(self):

        test_file_path = '/tmp/test_shell_util.txt'

        Path(test_file_path).unlink()

        command = "echo -n 'test2' > '{test_file_path}'".format(test_file_path=test_file_path)

        run(command)

        text = Path(test_file_path).read_text()

        self.assertEqual(text, 'test2')
