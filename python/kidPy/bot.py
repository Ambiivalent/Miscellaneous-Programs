import asyncio, discord, json
from lib import myClient

with open('config.json') as tokenData:
    token = json.load(tokenData)
    token = token["token"]

client = myClient()
client.run(token)
