# User collection testing
import requests
import json

base_URL = 'http://127.0.0.1:5000'

# Requests the card information from the database
# This is probably just here for testing tbh
def getCollection():
	url = base_URL + "/getCollection"
	
	r = requests.get(url)

	cardInfo = json.loads(r.content)
	return cardInfo

results = getCollection()
collection = results["collection"]
collect = json.loads(collection)

data = {"cards": []}
data["cards"] = collect

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
