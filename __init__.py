import skyscanner as sc


market = 'GB'
currency = 'GBP'
outbound = 'MANC'
inbound = 'GADA'
dateStart = '2018-12-10'
dateStop = '2018-12-24'
direct= False
apikey = 'ha626660336299059327728735244347'

one = sc.flight(market, currency, outbound, inbound, dateStart, dateStop, apikey,False)
print(one.cheapestFlight('2018-12-20'))