from .. import bot,openai_key
from telethon import events
import asyncio
import openai


openai.my_api_key=openai_key


@bot.on(events.NewMessage(incoming=True,pattern="/start"))
async def start(event):

 await event.reply("hello this is zarvis bot")
  
 
@bot.on(events.NewMessage(incoming=True,pattern="/get"))
async def start(event):
  a=await event.reply("hello this is get command")
 
  await a.edit("This is edited message")
  
  

@bot.on(events.NewMessage(incoming=True,pattern="/eval"))
async def start(event):
  await event.reply("hello this is eval command")