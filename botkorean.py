import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    await client.change_persence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
    if message.content.startswith("hi"):
        await message.channel.send("HI")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
