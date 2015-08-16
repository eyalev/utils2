import json

from .string_util import StringUtil
from .log_util import LogUtil
from bash import bash
from google.appengine.api import app_identity, urlfetch

# import share.lib.cloudstorage as gcs


def gcs_file(path):

    return GCSFileUtil(path).content()


def gcs_dict(path):

    return json.loads(gcs_file(path))


class GCSFileUtil(object):

    def __init__(self, full_path=None):
        self.full_path = self._validate(full_path)
        self.url = 'gs:/' + self.full_path
        self.storage_method = 'local'

    def write_from_file(self, file_path, header=None):

        command = 'gsutil {header} cp {file_path} {gcs_url}'.format(
            header=header,
            file_path=file_path,
            gcs_url=self.url
        )
        print(command)

        bash_result = bash(command)

        print(bash_result)

    def content(self):
        # if self.storage_method == 'local':
        #     return self.local_content()
        # elif self.storage_method == 'remote':
        return self.remote_content()

    def to_json_object(self):

        return StringUtil(self.content()).to_json_object()

    # def local_content(self):
    #     gcs_file = gcs.open(self.full_path)
    #     content = gcs_file.read()
    #     gcs_file.close()
    #     return content

    def remote_content(self):

        prod_url = 'http://storage.googleapis.com' + self.full_path
        LogUtil().info('GCSFile fetch: ' + prod_url)
        scope = 'https://www.googleapis.com/auth/devstorage.full_control'
        token, _ = app_identity.get_access_token(scope)
        response = urlfetch.fetch(
            prod_url,
            deadline=15,
            headers={'Authorization': 'OAuth %s' % token}
        )
        content = response.content

        return content

    # def write(self, content):
    #
    #     gcs_local_file = gcs.open(
    #         self.full_path,
    #         'w',
    #         content_type='text/plain',
    #     )
    #
    #     gcs_local_file.write(str(content))
    #
    #     gcs_local_file.close()

    def _validate(self, full_path):

        if full_path.startswith('gs://'):
            return full_path[4:]
        else:
            return full_path
