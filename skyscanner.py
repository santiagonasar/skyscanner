import json
import requests
from dataPull import browse

# URL to download json data from API
# url = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/GB/eur/en-GB/uk/pl/anytime/anytime?apikey=ha626660336299059327728735244347'

class flight():
    # Initialization of route.
    # Parameters must be passed to the class to specify, which parameters are to be observed
    # And which apikey should be used.
    # Initialization will later be passed to browse class in dataPull, as they are pretty
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

    # Within this method, data storing for single observed flight will be handled.
    # Maybe new class (datatype) should be defined to store it.
    def storeData(self):
        pass

    # This method will find cheapest flight on given date.
    # It will return data (dictionary?) to be stored.
    def cheapestFlight(self, date):
        pass

    # This method will run
    def searchFlights(self, start, stop):