import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if needsCorrecting(message.content):
        response = Corrector(message.content)
        await message.channel.send(response)

def needsCorrecting(message):
    count = 0
    for i in message:
        if (i == ' ' and count == 3):
            return True
        elif(i == ' '):
            count = 0
        else:
            count += 1
    if (count == 3):
        return True
    else:
        return False        

def Corrector(message):
    count = 0
    word = ""
    finalMessage = ""
    for i in message:
        print("Word: " + word)
        print("Letter: " + i)
        print("Final Message: " + finalMessage)
        print(count)

        if (i == ' ' and count == 3):
            count = 0
            finalMessage += "rat "
            word = ""
        elif(i == ' '):
            count = 0
            finalMessage += word
            finalMessage += ' '
            word = ""
        else:
            count += 1
            word += i
    if (count == 3):
        finalMessage += "rat"
    else:
        finalMessage += word
    return finalMessage


client.run(TOKEN)