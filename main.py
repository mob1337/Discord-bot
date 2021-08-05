import os
import discord
import re
import requests as req
import praw
from functions import topanime, anime_quotes, reply 
import time
client = discord.Client()
check_for_async=False
@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$leo'):
    await message.channel.send('Hello! {0.author.mention}'.format(message))
  if message.content.startswith('$topanime'):
    await message.channel.send('Based on my animelist')
    await message.channel.send('{0.author.mention} Here is the list'.format(message))
    await message.channel.send(topanime.top())
  if message.content.startswith('$say'):   
    await message.channel.send(re.sub(r'[()]','',"*"+str(anime_quotes.anime_quotes()))+"*")
  if message.content.startswith("$q"):
    b=message.content
    b=b.replace("$q","").strip()
    a=b.split(' ')
    b=a[0]
    h=a[1]
    g=a[2]
  
    #await message.channel.send(reply.Ask(b))
    dic=reply.Ask(b,h,int(g))
    count=1
    print(dic)
    for i in dic:
         await message.channel.send('Post: '+str(count)+''+i["title"]+"\n")
         if i['video_link'] == '':
           await message.channel.send(i["url_image"])
         else:
           await message.channel.send(i["video_link"])

         count=count+1
         time.sleep(0.5)
      
    
my_secret = os.environ['TOKEN'] + ''
client.run(my_secret)

