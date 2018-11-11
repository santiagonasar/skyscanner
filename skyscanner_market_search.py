apikey = "ha224559957686202721115639045827"

# We could actually get around the username for Skyscanner to get the cheapest cheapest option.
# Basically a hack.
# Look up everything, we wouldn't even need to use ML.

# ADD API KEY OTHERWISE WILL NOT WORK

import json
import requests
import pandas as pd

# Get requests, convert to dictionary.
quote_request = requests.get("http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/FR/eur/en-US/uk/us/anytime/anytime?apikey=" + apikey)
quotes_dic = quote_request.json()

# Get locales
locale_request = requests.get("http://partners.api.skyscanner.net/apiservices/reference/v1.0/locales?apiKey=" + apikey)
locale_dic = locale_request.json()


# Make them into a list so that we can go through them.

list_of_locales = []

for dic in locale_dic["Locales"]:
    list_of_locales.append(dic["Code"][3:])
    
print(list_of_locales)


# GOAL
# Scan through each quote and compare them to the other locales. 
# In the event there is a price difference, stop everything.
# Print out which locale has less price.

# Assumptions:
# From UK to France at anytime.

# PSUEDO-CODE
# The first market will be the comparison basis, in this case "LV" Latvia.
# Get the first quote's origin-destination. (We will go through every quote)

# For each origin-destination from the first country language:
url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/LV/eur/en-US/uk/fr/anytime/anytime?apikey=" + apikey
request = requests.get(url)
request_dic = request.json()

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
         org_name, "TO", dest_name)
        
    # For every locale starting from the second one:
    for locale in list_of_locales[2:]:
        # Get url locale.
        url = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/"
        url += locale
        url += "/eur/en-US/uk/fr/anytime/anytime?apikey=" + apikey

        # Print curent locale.
        print(locale)  

        # Request quotes. 
        quote_request = requests.get(url)
        quotes_dic = quote_request.json()

        # For every quote in quotes_dic
        for quote in quotes_dic["Quotes"]:
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