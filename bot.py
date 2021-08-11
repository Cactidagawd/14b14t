import discord
import requests
import json
import time
from collections import namedtuple
from datetime import date

client = discord.Client()

def responsedecoder(apidict): #json decoder 
    return namedtuple('X', apidict.keys())(*apidict.values())
@client.event
async def on_ready(): 
    print('Username: {0.user}\nId: {0.user.id}'.format(client)) #Logs in console the bots info
    activity = discord.Game(name="Prefix .") #var for presence
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
        currentdate = date.today() #var for current date
        dtformat = currentdate.strftime("Current date: %d/%m/%Y") #formats the date for the embed
        embedVar = discord.Embed(title="14b14t Stats", description="", color=0x0095ff) #embed var with the embed info
        embedVar.add_field(name=f"{dtformat}", value=f"Players: {players}\nMotd: {motd}\nOnline: {online}", inline=False) #Actually shows the stats and adds the fields
        await message.channel.send(embed=embedVar) #sends embed

    if message.content.startswith('.help'):
        embedVar = discord.Embed(title="14b14t Help", description="", color=0x0095ff) #embed var with the embed info
        embedVar.add_field(name="Normal Commands", value=".help\n.stats", inline=True) #normal command data
        embedVar.add_field(name="Staff Commands", value=".ban", inline=True) #staff command data
        await message.channel.send(embed=embedVar) #sends embed
 



client.run('') #put your token here
