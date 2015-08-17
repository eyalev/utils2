import sys
import distutils.sysconfig


class Util(object):

    def __init__(self):
        pass

    def print_paths(cls):
        print('\n'.join(sys.path))

    def packages_directory(self):
        print(distutils.sysconfig.get_python_lib())

    def cli_prompt(self):

        return __name__ == '__main__'

    def hello(self):

        print('Hello Util.')

if Util().cli_prompt():

    Util().hello()
