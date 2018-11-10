# -*- coding: utf-8 -*-

import requests
import json

# url = 'http://partners.api.skyscanner.net/apiservices/geo/v1.0?apikey=ha626660336299059327728735244347'

# takes in url and returns dictionary pulled from API
class browse:
    def __init__(self, market, currency, outbound, inbound,
                 dateStart, dateStop, direct=false, apikey):
        # /GB/eur/en-GB/uk/pl/anytime/anytime?apikey=ha626660336299059327728735244347'
        self.market = market
        self.outbound = outbound
        self.inbound = inbound
        self.direct = direct
        self.currency = currency
        self.apikey = apikey
        self.dateStart = dateStart
        self.dateStop = dateStop
        self.dateReturn = ''

    # Function returns browseQuotes query result
    def getQuotes(url):
        pulledData = requests.get(url)
        pulledDict = pulledData.json()
        return pulledDict


    # Function prepares URL to pass to getQuotes
    # Uses variables passed to class to determine which parameters are relevant
    # Has to return url (query) which will return proper record
    def prepareURL(self):
        # Sample URL part two
        # /GB/eur/en-GB/uk/pl/anytime/anytime?apikey=ha626660336299059327728735244347'

        url = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0'
        url += '/' + self.market
        url += '/' + self.currency
        url += '/en-GB'
        url += '/' + self.outbound
        url += '/' + self.inbound
        url += '/' + outboundDate
        url += '/'
        url += '?apikey=' + self.apikey
        return url
