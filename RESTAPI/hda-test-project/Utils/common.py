import pytest
import requests
import csv
import sys
import logging
import os
import json
import inspect
import pdb

# print(sys.version_info)
if sys.version_info < (3,7):
    raise Exception("Requires Python 3.7 or above.")

LOG_LEVEL = logging.INFO # DEBUG, INFO, WARNING, ERROR, CRITICAL
common_formatter = logging.Formatter('%(asctime)s [%(levelname)-7s][ln-%(lineno)-3d]: %(message)s', datefmt='%Y-%m-%d %I:%M:%S')

root_path = os.path.dirname( os.path.dirname(os.path.realpath(__file__)) )
# pdb.set_trace()


def setup_logger(log_file, level=logging.INFO, name='', formatter=common_formatter):
    """Function setup as many loggers as you want."""
    handler = logging.FileHandler(log_file,mode='w') # default mode is append
    # Or use a rotating file handler
    # handler = RotatingFileHandler(log_file,maxBytes=1024, backupCount=5)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# logger for API outputs
api_formatter = logging.Formatter('%(asctime)s: %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
api_outputs_filename = root_path + os.sep + 'Logs' + os.sep + 'api_outputs.log'
log_api = setup_logger(api_outputs_filename, LOG_LEVEL,'log_api',formatter = api_formatter)

# pretty print Restful request to API log
# argument is request object
def pretty_print_request(request):
    """
    Pay attention at the formatting used in this function because it is programmed to be pretty printed and may differ from the actual request.
    """
    log_api.info('{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
        )

# pretty print Restful response to API log
# argument is response object
def pretty_print_response(response):
    log_api.info('{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text
        ))



# argument is response object
# display body in json format explicitly with expected indent. Actually most of the time it is not very necessary because body is formatted in pretty print way.
def pretty_print_response_json(response):
    """ pretty print response in json format.
        If failing to parse body in json format, print in text.
    """
    try:
        resp_data = response.json()
        resp_body = json.dumps(resp_data,indent=4)
    # if .json() fails, ValueError is raised.
    except ValueError:
        resp_body = response.text
    log_api.info('{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        resp_body
        ))


def get(url, auth=None, verify=False):
    """
    common request get function with below features, which you only need to take care of url:
        - print request and response in API log file
        - Take care of request exception and non-200 response codes and return None, so you only need to care normal json response.
        - arguments are the same as requests.get

    verify: False - Disable SSL certificate verification
    """
    try:
        if auth == None:
            resp = requests.get(url, verify=verify)
        else:
            resp = requests.get(url, auth=auth, verify=verify)
            assert resp.headers["Content-Type"] == "application/json"
    except Exception as ex:
        log.error('requests.get() failed with exception:', str(ex))
        return None

    # pretty request and response into API log file
    pretty_print_request(resp.request)
    pretty_print_response_json(resp)

    # This return caller function's name, not this function post.
    caller_func_name = inspect.stack()[1][3]
    if resp.status_code != 200:
        log.error('%s failed with response code %s.' % (caller_func_name, resp.status_code))
        return None
    return resp.json()

def post(url, data, headers={}, verify=False, amend_headers=True):
    """
    common request post function with below features, which you only need to take care of url and body data:
        - append common headers
        - print request and response in API log file
        - Take care of request exception and non-200 response codes and return None, so you only need to care normal json response.
        - arguments are the same as requests.post, except amend_headers.

    verify: False - Disable SSL certificate verification
    """

    # append common headers if none
    headers_new = headers
    if amend_headers == True:
        if 'Content-Type' not in headers_new:
            headers_new['Content-Type'] = r'application/json'
        if 'User-Agent' not in headers_new:
            headers_new['User-Agent'] = 'Python Requests'

    # send post request
    resp = requests.post(url, json=data, headers=headers_new, verify=verify)

    # pretty request and response into API log file
    # Note: request print is common instead of checking if it is JSON body. So pass pretty formatted json string as argument to the request for pretty logging.
    pretty_print_request(resp.request)
    pretty_print_response_json(resp)

    # This return caller function's name, not this function post.
    caller_func_name = inspect.stack()[1][3]
    if resp.status_code != 200:
        log.error('%s failed with response code %s.' % (caller_func_name, resp.status_code))
        return None
    return resp

def read_data_from_csv(filename):
    test_data_users_from_csv = []
    with open(filename, newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        for row in data:
            test_data_users_from_csv.append(row)
    return test_data_users_from_csv


def create_hotel_compset_watcher_json_object():
    return [
        {
            "messageId": "12345FRT55421356",
            "hoodId": "89686",
            "starRating": "2.5",
            "percentRecommended": "85",
            "lodgingTypeCode": "H",
            "startDate": "2020-11-09",
            "endDate": "2020-11-12",
            "numOfRooms": "1",
            "numOfAdults": "2",
            "numOfChildren": "0",
            "destination": "Miami, FL",
            "hoodName": "Miami Intl Airport (MIA) West - Doral",
            "gaiaId": "",
            "amount": "78.9999985",
            "currencyCode": "USD"
        }
    ]


def create_car_compset_watcher_json_object():
    return [
        {
            "messageId": "12345FRT55456",
            "amount": "61.24",
            "currencyCode": "USD",
            "updateTime": "2020-09-05",
            "startDate": "2020-11-10",
            "endDate": "2020-11-15",
            "strikeThroughPrice": "0.0",
            "carTypeCode": "CCAR",
            "rateType": "RETAIL",
            "rentalAgencyCode": "ZE",
            "startAirportCode": "JFK",
            "destinationAirportCode": "JFK",
            "startAirportName": "New York John F Kennedy Intl.(JFK)",
            "destinationAirportName": "New York John F Kennedy Intl.(JFK)",
            "models": "Nissan Versa or similar",
            "carTypeName": "Compact"
        }
    ]

