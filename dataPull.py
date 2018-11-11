# -*- coding: utf-8 -*-

import requests
import json

# url = 'http://partners.api.skyscanner.net/apiservices/geo/v1.0?apikey=ha626660336299059327728735244347'

# takes in url and returns dictionary pulled from API
class Browse:
    def __init__(self, market, currency, outbound, inbound,
                 apikey, direct= False):
        # /GB/eur/en-GB/uk/pl/anytime/anytime?apikey=ha626660336299059327728735244347'
        self.market = market
        self.outbound = outbound
        self.inbound = inbound
        self.direct = direct
        self.currency = currency
        self.apikey = apikey

    # Method returns browseQuotes query result
    # That is dictionary with four entries:
    # Quotes, Places, Carriers, Currencies. Each of these contains a list of dictionaries.
    #
    def getQuotes(self, url):
        pulledData = requests.get(url)
        pulledDict = pulledData.json()
        return pulledDict


    # Method prepares URL to pass to getQuotes
    # Uses variables passed to class to determine which parameters are relevant
    # Has to return url (query) which will return proper record
    def prepareURL(self, outboundDate):
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

    # Method is passed dictionary from getQuotes. Returns the data it was supposed to retrieve,
    # as list (possibly with dictionaries
    def retrieveData(self, data):
        flights = []
        for element in data['Quotes']:
            # appends ONLY prices of the list. In the future other features should be added
            # carriers, exact dates, etc.
            flights.append(element['MinPrice'])
        flights.sort()
        return flights

    # What will be returned from retrievedData will be encrypted with scyscanner's IDs.
    # This method is to decrypt it; keys are provided in the dictionary returned by getQuotes.
    def decryptIDs(self):
        pass