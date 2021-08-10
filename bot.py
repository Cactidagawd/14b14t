import discord
import requests
import json
from collections import namedtuple
client = discord.Client()

def responsedecoder(apidict): #json decoder 
    return namedtuple('X', apidict.keys())(*apidict.values())
@client.event
async def on_ready(): 
    print('Username: {0.user}\nId: {0.user.id}'.format(client)) #Logs in console the bots info
    activity = discord.Game(name=".stats") #var for presence
    await client.change_presence(status=discord.Status.idle, activity=activity) #sets presence

@client.event
async def on_message(message): #listens to messages being sent
    if message.author == client.user: #checks if the message sender is the bot
        return #returns
    if message.content.startswith('.stats'): #if the message that is sent starts with .stats it will procced with the api requests
        response = requests.get('https://mcapi.us/server/status?ip=14b14t.com') #request api
        apiresponsetext = response.text #variable to make my life easier
        server = json.loads(apiresponsetext, object_hook=responsedecoder) #decodes json and is under the var server to make my life easier
        players = server.players.now #var for player count
        motd = server.motd #var for player count
        online = server.online #var for online count
        embedVar = discord.Embed(title="14b14t Stats", description="", color=0x0095ff) #embed var with the embed info
        embedVar.add_field(name="Players:", value=players, inline=False) #Actually shows the stats and adds the fields
        embedVar.add_field(name="Motd:", value=motd, inline=False) #Actually shows the stats and adds the fields
        embedVar.add_field(name="Online", value=online, inline=False) #Actually shows the stats and adds the fields
        await message.channel.send(embed=embedVar) #sends embed


client.run('') #put your token here