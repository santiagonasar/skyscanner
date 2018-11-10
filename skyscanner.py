import json
import requests
import dataPull as dp

# URL to download json data from API
url = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/GB/eur/en-GB/uk/pl/anytime/anytime?apikey=ha626660336299059327728735244347'

data = dp.get(url)

class route():
    One two threeg