import requests

data=requests.get("https://xkcd.com/1906/")

print(data.text)