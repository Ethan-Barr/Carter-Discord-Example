import json

with open('tokens.json', 'r') as f:
    data = json.load(f)


DiscordAPI = data['token']
APIkey = data['carterKey']
UIName = data['name']
Prefix = data['prefix']
ModLog = data['modLog']
IgnoredNames = ["Ultron#1582"]


# print(DiscordAPI, APIkey, UIName, Prefix)
