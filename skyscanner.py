import json
import requests
import time
from dataPull import Browse
from datetime import datetime
from datetime import timedelta


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

    # This method will run
    def searchFlights(self):
        start = datetime.strptime(self.dateStart, '%Y-%m-%d')
        stop = datetime.strptime(self.dateStop, '%Y-%m-%d')
        flights = {}
        while start <= stop:
            dateString = start.strftime("%Y-%m-%d")
            flights[dateString]=self.cheapestFlight(dateString)
            start = start + timedelta(days=1)
        return flights

    # def cheapestFlight(self, date):
    #     """
    #     We could actually get around the username for Skyscanner to get the cheapest cheapest option.
    #     Basically a hack.
    #     Look up everything, we wouldn't even need to use ML.
        
    #     !ADD API KEY OTHERWISE WILL NOT WORK!
    #     """
    #     list_of_locales = self.pull.getLocales()

    #     # GOAL
    #     # Scan through each quote and compare them to the other locales. 
    #     # In the event there is a price difference, stop everything.
    #     # Print out which locale has less price.

    #     # Assumptions:
    #     # From UK to France at anytime.

    #     # PSUEDO-CODE
    #     # The first market will be the comparison basis, in this case "LV" Latvia.
    #     # Get the first quote's origin-destination. (We will go through every quote)

    #     # For each origin-destination from the first country language:

    #     request_dic = Browse("LV", self.currency, self.outbound, self.inbound, date, self.apikey).getJSON()

    #     for quote in request_dic["Quotes"]:
    #         # Store quote origin and destination as "basis_org_loc" and "basis_dest_loc".
    #         basis_org_loc = quote["OutboundLeg"]["OriginId"]
    #         basis_dest_loc = quote["OutboundLeg"]["DestinationId"]
            
    #         # Get real names rather than Id's.
    #         for place in request_dic["Places"]:
    #             if place["PlaceId"] == basis_org_loc:
    #                 org_name = place["Name"]
    #             elif place["PlaceId"] == basis_dest_loc:
    #                 dest_name = place["Name"]
            
    #         # Store price in "minnest_price".
    #         minnest_price = quote["MinPrice"]
            
    #         print("CHECKING MARKETS FOR FLIGHTS FROM",
    #             org_name, "TO", dest_name)
                
    #         # For every locale starting from the second one:
    #         for locale in list_of_locales[2:]:
    #             # Get url locale.
    #             url = Browse(locale, self.currency, self.outbound, self.inbound, date, self.apikey).getURL()

    #             # Print curent locale.
    #             print(locale)  

    #             # Request quotes. 
    #             quote_request = requests.get(url)
    #             quotes_dic = quote_request.json()

    #             # For every quote in quotes_dic
    #             for quote in quotes_dic["Quotes"]:
    #                 # If quote's origin-destination same as "basis_loc":
    #                 if (quote["OutboundLeg"]["OriginId"] == basis_org_loc and
    #                     quote["OutboundLeg"]["DestinationId"] == basis_dest_loc):
    #                     # If price is less than minnset_price:
    #                     if quote["MinPrice"] < minnest_price:                    
    #                         # print out PRICE IS LESS!!
    #                         print("PRICE IS LESS!!!")
    #                         # print out old and new price.
    #                         print("FROM", org_name, "TO", dest_name)
    #                         print("CHEAPER FOR", locale, "USERS FOR THAN THE OTHERS")
    #                         print(quote["MinPrice"], minnest_price)
                            
    #                         minnest_price = quote["MinPrice"]
                            
    #                         # STOP EVERYTHING!
    #                         #raise SystemExit("STOP EVERYTHING")
    #         print()

        
    def cheapestFlight(self, outboundDate):
        # GOAL
        # Scan through each quote and compare them to the other locales. 
        # In the event there is a price difference, stop everything.
        # Print out which locale has less price.

        # ASSUMPTIONS:
        # From UK to France at anytime.

        # PSUEDO-CODE
        # The first market will be the comparison basis, in this case "LV" Latvia.
        # Get the first quote's origin-destination. (We will go through every quote)

        # VARIABLES
        # Translates to:
        # I want to go from the UK to France on the 9th of January
        # Paying in Euros. What is the cheapest market I should sign up with?

        # Make them into a list so that we can go through them.

        def getLocales():
            locale_request = requests.get("http://partners.api.skyscanner.net/apiservices/reference/v1.0/locales?apiKey=" + self.apikey)
            locale_dic = locale_request.json()

            # Make them into a list so that we can go through them.

            list_of_locales = []

            for dic in locale_dic["Locales"]:
                list_of_locales.append(dic["Code"][3:])

            return list_of_locales

        list_of_locales = getLocales()
        print(list_of_locales)

        # Now to use the locales

        def getURL(market, currency, outbound, inbound, outboundDate, apikey):
            # Sample URL part two
            # /GB/eur/en-GB/uk/pl/anytime/anytime?apikey=ha626660336299059327728735244347'

            url = 'http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0'
            url += '/' + market
            url += '/' + currency
            url += '/en-GB'
            url += '/' + outbound
            url += '/' + inbound
            url += '/' + outboundDate
            url += '/'
            url += '?apikey=' + apikey
            return url

        def getJSON(url):
            pulledData = requests.get(url)
            pulledDict = pulledData.json()
            return pulledDict

        # For each origin-destination from the first country language:
        url = getURL("LV", self.currency, self.outbound, self.inbound, outboundDate, self.apikey)
        request_dic = getJSON(url)

        #! TODO
        # Don't go through every quote, get the origin and destination the user requests.
        # Make more methods.


        for quote in request_dic["Quotes"]:
            # Store quote origin and destination as "basis_org_loc" and "basis_dest_loc".
            basis_org_loc = quote["OutboundLeg"]["OriginId"]
            basis_dest_loc = quote["OutboundLeg"]["DestinationId"]
            
            # Get real names rather than Id's.
            for place in request_dic["Places"]:
                if place["PlaceId"] == basis_org_loc:
                    org_name = place["Name"]
                elif place["PlaceId"] == basis_dest_loc:
                    dest_name = place["Name"]
            
            # Store price in "minnest_price".
            minnest_price = quote["MinPrice"]
            
            print("CHECKING MARKETS FOR FLIGHTS FROM",
                org_name, "TO", dest_name, "ON", outboundDate)
                
            # For every locale starting from the second one:
            for index, locale in enumerate(list_of_locales[2:]):
                # Get url locale.
                url = getURL(locale, self.currency, self.outbound, self.inbound, outboundDate, self.apikey)

                # Print curent locale.
                # print(locale) 
                
                # Print markets checked
                print(index+1, "OUT OF", 42, "CHECKED")
                print(str(int((index+1) / 42 * 100)) + "%")
                
                # Request quotes. 
                request_rest_dic = getJSON(url)

                # For every quote in quotes_dic
                for quote in request_rest_dic["Quotes"]:
                    time.sleep(0.12)
                    # If quote's origin-destination same as "basis_loc":
                    if (quote["OutboundLeg"]["OriginId"] == basis_org_loc and
                        quote["OutboundLeg"]["DestinationId"] == basis_dest_loc):
                        # If price is less than minnset_price:
                        if quote["MinPrice"] < minnest_price:                    
                            # print out PRICE IS LESS!!
                            print("PRICE IS LESS!!!")
                            # print out old and new price.
                            print("FROM", org_name, "TO", dest_name)
                            print("CHEAPER FOR", locale, "USERS FOR THAN THE OTHERS")
                            print(quote["MinPrice"], minnest_price)
                            
                            minnest_price = quote["MinPrice"]

                            return minnest_price
                            
                            # STOP EVERYTHING!
                            #raise SystemExit("STOP EVERYTHING")
            print()

        return minnest_price