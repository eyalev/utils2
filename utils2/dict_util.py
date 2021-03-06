from collections import OrderedDict
import json

odict = OrderedDict


class DictUtil(object):

    def __init__(self, _dict):
        self._dict = _dict

    def sorted(self):
        return odict(sorted(self._dict.items()))

    @classmethod
    def merge(cls, *dict_args):
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result

    def key_value_tuples(self):

        return [(key, value) for key, value in self._dict.iteritems()]

    def key_value_output(self):

        output = ''
        for _tuple in self.key_value_tuples():
            output += str(_tuple)
            output += '\n'

        return output

    def to_json_string(self):

        return json.dumps(self._dict)

    def to_pretty_json_string(self):

        return json.dumps(self._dict, indent=4)

    def sort_od(self, _odict):
        res = odict()
        for k, v in sorted(_odict.items()):
            if isinstance(v, dict):
                res[k] = self.sort_od(v)
            else:
                res[k] = v
        return res
