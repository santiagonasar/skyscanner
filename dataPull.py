# -*- coding: utf-8 -*-

import requests
import json

# url = 'http://partners.api.skyscanner.net/apiservices/geo/v1.0?apikey=ha626660336299059327728735244347'

# takes in url and returns dictionary pulled from API
class one:
    def __init__(self, market, outbound, destination, direct=false, currency):
        self.market = market
        self.outbound = outbound
        self.destination = destination
        self.direct = direct
        self.currency = currency

    # Function returns browseQuotes query result
    def getQuotes(url):
        pulledData = requests.get(url)
        pulledDict = pulledData.json()
        return pulledDict

    # Function prepares URL to pass to getQuotes
    # Uses variables passed to class to determine which parameters are relevant
    # Has to return url (query) which will return proper record
    def prepareURL(self):
