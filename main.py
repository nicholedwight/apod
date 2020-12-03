import urllib.request
import json
import yaml

from credentials import API_KEY
from datetime import date

today = date.today()


url = 'https://api.nasa.gov/planetary/apod?'
api = 'api_key=' + API_KEY

urlobj = urllib.request.urlopen(url + api)

read = urlobj.read()

decode = json.loads(read.decode('utf-8'))


with open('apod-dump.json', 'r') as file:
    data = json.loads(file.read())
    for key, value in data.items():
        if key == 'date':
                if value == str(today):
                    # Don't duplicate a day's data
                    file.close()
                else:
                    # Appending new date's data to json file
                    file = open('apod-dump.json', 'a')
                    json.dump(decode, file, ensure_ascii=False)
                    file.close()
