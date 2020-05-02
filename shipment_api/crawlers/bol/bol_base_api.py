import time
import requests

from ..base.base_api import BaseAPI


class BolBaseAPI(BaseAPI):

    def get_url(self) -> str:
        return 'https://api.bol.com/retailer'

    def process_import(self, params) -> int:
        pass

    def make_api_call(self, url, params, token):
        headers = {
            'Accept': 'application/vnd.retailer.v3+json',
            'Authorization': 'Bearer %s' % token
        }
        try:
            response = requests.get(url, params=params, headers=headers)

            return response.json()
        except:
            pass
