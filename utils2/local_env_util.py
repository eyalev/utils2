from .log_util import LogUtil
from .file_util import FileUtil


class LocalEnvUtil(object):

    def __init__(self, env_file_path='env/env.json'):

        self.env_file_path = env_file_path
        self.env_dict = self.init_env_dict()

    def init_env_dict(self):

        try:
            return FileUtil(self.env_file_path).to_dict()

        except IOError:
            LogUtil().info(self.env_file_path + ' not found.')
            return {}

    def get(self, name, default=None):

        try:
            value = self.env_dict[name]
            return value

        except KeyError:
            return default
