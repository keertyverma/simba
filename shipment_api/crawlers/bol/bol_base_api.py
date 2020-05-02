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

            if response.status_code == 429:
                print('Sleeping...%s' % str(response.headers))
                time.sleep(int(response.headers['retry-after']))

                response = requests.get(url, params=params, headers=headers)

            return response.json()
        except Exception as e:
            print('request %s' % e)
