import discord 
import json 
import re

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    text=re.search('^!(zote|precept)[" "]*\d{1,2}',message.content.lower())

    if(text):

        precept=int(re.search('\d{1,2}',text.group()).group())
        precepts=json.load(open("./precepts.json"))
        if precept <=len(precepts) and precept>0:


            await message.channel.send(precepts[precept-1])


client.run('')