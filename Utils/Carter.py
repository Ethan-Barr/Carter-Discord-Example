import requests
import json

from Utils.secret import carterAPI

def CarterSend(sentence, userID):
    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "content-Type": "application/json"
    }, data=json.dumps({
        "text": sentence,
        "key": carterAPI,
        "playerId": userID
    }))

    CarterResponse = response.json()["output"]["text"]

    f = open("CarterResponse.txt", "w+")
    f.write(f"{CarterResponse}")
    f.close()