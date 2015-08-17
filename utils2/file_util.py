import json
import codecs

from bash import bash
from .gcs_file_util import GCSFileUtil


class FileUtil(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path) as _file:
            data = _file.read()

        return data

    def to_dict(self):
        with open(self.file_path) as json_data:
            dict_data = json.load(json_data)

        return dict_data

    def to_json(self):
        return json.dumps(self.to_dict())

    def write(self, string):

        with open(self.file_path, 'w') as file_object:
            file_object.write(string)

    def write_utf8(self, string):

        with codecs.open(self.file_path, 'w', "utf-8-sig") as file_object:
            file_object.write(string)

    def write_with_curl_from(self, url):

        command = "curl '{url}' -o {file_path}".format(
            url=url,
            file_path=self.file_path
        )

        print(command)

        bash_result = bash(command)

        print(bash_result)

    def write_to_gcs(self, gcs_file_url):

        GCSFileUtil(gcs_file_url).write(self.file_path)
