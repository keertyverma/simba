from __future__ import absolute_import, unicode_literals
import logging
import copy
from celery import shared_task

from .crawlers.bol.bol_shipment_list_api import BolShipmentListAPI
from .crawlers.bol.bol_shipment_api import BolShipmentAPI


logger = logging.getLogger(__name__)


@shared_task
def trigger_shipment_import(shop_type, client_credentials):
    # return response to import_data task
    # call import_shipment_by_ID task per shipment ID
    # if rate limit exceed then wait till its expiration periods is over
    # handle token generation : if expired then get new token and queue task again
    # if shipment date is greater then one exising in DB then only run import_shipment_by_ID task
    payload = {
        'token': '',
        'last_updated_at': None,
        'page': 1,
        'client_id': client_credentials['client_id']
    }
    fulfilment_method = ['FBB', 'FBR']

    for ffm in fulfilment_method:
        new_payload = copy.deepcopy(payload)
        new_payload['fulfilment_method'] = ffm
        import_data.delay('BolShipmentListAPI', new_payload)


@shared_task
def import_data(class_name, payload):
    python_class = globals()[class_name]
    api_object = python_class()
    new_tasks = api_object.process_import(payload)

    for new_task in new_tasks:
        import_data.delay(new_task['class_name'], new_task['payload'])
