import json
import requests
import time

apikey = "ha224559957686202721115639045827"

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
currency = "eur"
outbound = "uk"
inbound = "fr"
outboundDate = "2019-08-10"
apikey = "ha626660336299059327728735244347"

# Make them into a list so that we can go through them.

def getLocales():
    locale_request = requests.get("http://partners.api.skyscanner.net/apiservices/reference/v1.0/locales?apiKey=" + apikey)
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
url = getURL("FR", currency, outbound, inbound, outboundDate, apikey)
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
        url = getURL(locale, currency, outbound, inbound, outboundDate, apikey)

        # Print curent locale.
        # print(locale) 
        
        # Print markets checked
        print(index+1, "OUT OF", 42, "CHECKED")
        print(str(int((index+1) / 42 * 100)) + "%")
        
        # Request quotes. 
        request_rest_dic = getJSON(url)

        # For every quote in quotes_dic
        for quote in request_rest_dic["Quotes"]:
            #time.sleep(0.01)
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
                    
                    # STOP EVERYTHING!
                    #raise SystemExit("STOP EVERYTHING")
    print()