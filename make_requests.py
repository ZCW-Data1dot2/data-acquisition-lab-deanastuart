import requests
import json
import os
json_file_count = 0
url_offset = 1


token = input('Token:')
payload = {}
headers = {
  'Content-Type': 'application/json',
  'token': token,
  'Authorization': 'Bearer' + token
}

# data = (response.text.encode('utf8'))

def write(jsonfile, data):
    with open(jsonfile, 'w') as outfile:
        json.dump(data, outfile)

for i in range(0,39):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?limit=1000&offset=" + str(url_offset)
    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.json()
    jsonfile = "/Users/deana/Documents/Projects/data-acquisition-lab-dstuart/locations/locations_" + str(json_file_count) + ".json"
    write(jsonfile, data)
    json_file_count += 1
    url_offset += 1000