from datetime import datetime
import json
import urllib

from dateutil import parser
from utils2.datetime_util import DatetimeUtil
from utils2.string_base_util import StringBaseUtil


class StringUtil(object):

    def __init__(self, string):
        self.string = string

    def to_date(self):
        return datetime.strptime(self.string, '%Y-%m-%d').date()

    def to_datetime(self):
        return StringBaseUtil(self.string).to_datetime()

    def to_pretty_datetime(self):
        dt = parser.parse(self.string).replace(tzinfo=None)
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    def to_datetime_iso(self):
        dt = parser.parse(self.string).replace(tzinfo=None)
        return dt.strftime('%Y-%m-%dT%H:%M:%S')

    def to_json(self):

        return json.loads(self.string)

    to_json_object = to_json

    def url_encode(self):

        return urllib.quote_plus(self.string)

    def url_decode(self):

        return urllib.unquote_plus(self.string)

    def add(self, timedelta):

        new_dt = self.to_datetime() + timedelta
        dt_string = DatetimeUtil(new_dt).to_iso_format()

        return dt_string

    def remove_new_lines(self):

        return self.string.replace('\n', '')
