import json
import requests
from dataPull import Browse

# URL to download json data from API
# url = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/GB/eur/en-GB/uk/pl/anytime/anytime?apikey=

class flight():
    # Initialization of route.
    # Parameters must be passed to the class to specify, which parameters are to be observed
    # And which apikey should be used.
    def __init__(self, market, currency, outbound, inbound,
                 dateStart, dateStop, apikey, direct= False):
        # /GB/eur/en-GB/uk/pl/anytime/anytime?apikey=api
        self.market = market
        self.outbound = outbound
        self.inbound = inbound
        self.direct = direct
        self.currency = currency
        self.apikey = apikey
        self.dateStart = dateStart
        self.dateStop = dateStop
        self.dateReturn = ''
        self.pull = Browse(self.market, self.currency, self.outbound, self.inbound,
                      self.apikey, False)

    # Within this method, data storing for single observed flight will be handled.
    # Maybe new class (datatype) should be defined to store it.
    def storeData(self):
        pass

    # This method will find cheapest flight on given date.
    # It will return data (dictionary?) to be stored.
    def cheapestFlight(self, date):
        url = self.pull.prepareURL(date)
        dict = self.pull.getQuotes(url)
        cheapest = self.pull.retrieveData(dict)
        return cheapest[0]

    # This method will run
    def searchFlights(self, start, stop):
        pass