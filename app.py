import os
import json
from flask import Flask, jsonify, request
import random
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType, InteractionResponseFlags

CLIENT_PUBLIC_KEY = ""
PRECEPTS=json.load(open("./precepts.json"))


app = Flask(__name__)

def get_precepts(number:int):
    if number not in range(1,len(PRECEPTS)+1):
        return PRECEPTS[random.randint(0,len(PRECEPTS))-1]
    else:
        return PRECEPTS[number-1]

@app.route('/interactions', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def interactions():
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:
        print(request)
        try:
            return jsonify({
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content':  get_precepts(request.json['data']["options"][0]["value"])
            }
            })
        except:
            return jsonify({
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content':  PRECEPTS[random.randint(0,len(PRECEPTS))-1]
            }
            })

@app.get("/")
def uga():
  return "Uga"

if __name__=="__main__":
  app.run(port=5000)