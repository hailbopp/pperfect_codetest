#!/usr/bin/env python3
from __future__ import print_function, unicode_literals

import sys

import requests


def is_service_responding(url: str) -> bool:
    """
    Checks whether a service at host `url` is responding to requests. Uses the API at api.downfor.cloud.
    :param url: the domain name to check
    :return: a boolean indicating whether the service is responding
    """
    headers = {
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://downforeveryoneorjustme.com/{0}'.format(url),  # Yes, I know Referrer is misspelled. That's
                                                                           # just how the API works, I guess.
        'Origin': 'https://downforeveryoneorjustme.com',
        'User-Agent': 'Mozilla/5.0 PPerfectEval',
    }

    # This responds with a JSON body of the following shape:
    # {
    #   "statusCode":int,
    #   "statusText": str,
    #   "isDown": bool,
    #   "returnedUrl": str,
    #   "requestedDomain": str,
    #   "lastChecked": int
    # }
    try:
        response = requests.get('https://api.downfor.cloud/httpcheck/{0}'.format(url), headers=headers)
        return not response.json()['isDown']
    except:
        print("Could not complete request.")
        raise


def main(url: str):
    responding = is_service_responding(url)
    print("{0} is {1} to requests".format(url, "responding" if responding else "not responding"))


if __name__ == '__main__':
    domain = None
    try:
        domain = sys.argv[1]
    except:
        print("Usage: {0} domain.com".format(sys.argv[0]))
        raise

    main(domain)
