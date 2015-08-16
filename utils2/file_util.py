import json


class FileUtil(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def to_dict(self):
        with open(self.file_path) as json_data:
            dict_data = json.load(json_data)

        return dict_data

    def to_json(self):
        return json.dumps(self.to_dict())

    def write(self, string):

        with open(self.file_path, 'w') as file_object:
            file_object.write(string)
