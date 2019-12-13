import discord
import os
import configparser

client = discord.Client()


@client.event
async def on_ready():
    a = configparser.ConfigParser()
    a.read("krsetting.ini")
    status = a["설정"]["상태"]
    print(client.user.id)
    print("ready")
    game = discord.Game(status)
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    setting = configparser.ConfigParser()
    rosbot = configparser.ConfigParser()
    setting.read("krsetting.ini")
    rosbot.read("krsetting.ini")
    hud = setting["허드"]["상태"]
    if message.content.startswith("허드패치"):
        await message.channel.send(hud)

    if message.content.startswith("허드업뎃"):
        await message.channel.send(hud)

    if message.content.startswith("허드되나요"):
        await message.channel.send(hud)

    if message.content.startswith("터보허드"):
        await message.channel.send(hud)

    rosbot = setting["로스봇"]["상태"]
    if message.content.startswith("로스봇"):
        await message.channel.send(rosbot)
    
    if message.content.startswith("로스봇패치"):
        await message.channel.send(rosbot)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
