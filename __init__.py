import skyscanner as sc


market = 'GB'
currency = 'GBP'
outbound = 'MANC'
inbound = 'GADA'
dateStart = '2018-12-10'
dateStop = '2018-12-24'
direct= False
with open('api.txt', mode='r') as file:
    apikey = file.read()

one = sc.flight(market, currency, outbound, inbound, dateStart, dateStop, apikey,False)
print(one.searchFlights())