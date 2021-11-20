import requests
import json
from requests.packages.urllib3.util.retry import Retry
from api.utilities import TimeoutHTTPAdapter


#
# Atualiza aplica sistema Analytics
#


def consumeAnalytcs(params):
    """
    name: consumeAnalytcs
    :param params: Any
    :return:
    """

    json_ = json.dumps(params)
    jsonload_ = json.loads(json_)

    url_ = 'http://127.0.0.1:8002/analytics/v1/newsbulk/'
    headers_ = {"Accept": "application/json"}

    retries_ = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])

    adapter_ = TimeoutHTTPAdapter(max_retries=retries_)

    session_ = requests.Session()
    session_.mount('http://http://127.0.0.1:8002/analytics/', adapter_)
    session_.mount('https://http://127.0.0.1:8002/analytics/', adapter_)

    try:
        request_ = session_.post(url_, headers=headers_, json=params, auth=("admin", "Ab041972@"))
        request_.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)



# 500 error: Internal Server Error
# 502 error: Bad Gateway
# 503 error: Service Unavailable
# 504 error: Server is unavailable
# _Session.mount('ftp://', FTPAdapter()
