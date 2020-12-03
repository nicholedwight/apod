import urllib.request
import json

from credentials import API_KEY


url = 'https://api.nasa.gov/planetary/apod?'
api = 'api_key=' + API_KEY

urlobj = urllib.request.urlopen(url + api)

read = urlobj.read()

decode = json.loads(read.decode('utf-8'))

print(decode)