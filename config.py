import json
import os

with open('config.json', 'r') as f:
    config = json.load(f)


token = config['token']
prefix = config['prefix']
carterKey = config['carterKey']