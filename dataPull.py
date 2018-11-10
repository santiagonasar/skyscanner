# -*- coding: utf-8 -*-
import json
import requests


# url = 'http://partners.api.skyscanner.net/apiservices/geo/v1.0?apikey=ha626660336299059327728735244347'

# takes in url and returns dictionary pulled from API
def geo(url):
    geoData = requests.get(url)
    geoDict = geoData.json()
    return geoDict




"""
with open('continents.txt', mode='w') as file:
	for element in geoDict["Continents"]:
		for element2 in element['Countries']:
			file.write(element["Id"] + " " + element["Name"])
			file.write('\n')
"""
"""
for element in geoDict['Continents']:
	print(element['Countries'])
"""
"""
with open('geo.txt', mode='w') as file:
	for element in geoDict:
		file.write(json.dumps(element, ensure_ascii=False))
		file.write('\n')
"""
"""
for value1 in localesDict.values():
	print(value2.type(), end='\n')
"""