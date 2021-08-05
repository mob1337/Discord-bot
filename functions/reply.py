import os
import os
import praw
import discord
from datetime import datetime

pwdd  = os.environ['password'] #PUT YOUR REDDIT DEVELOPER PASSWORD
uname  = os.environ['username']  #PUT YOUR REDDIT DEVELOPER USERNAME
agent  = os.environ['user_agent']  #PUT YOUR REDDIT DEVELOPER USER_AGENT
clientKey  = os.environ['clientkey']  #PUT YOUR REDDIT DEVELOPER CLIENTKEY
client_id  = os.environ['client_ID'] #PUT YOUR REDDIT DEVELOPER client_ID

#below function converts the posts into JSON/KEY-VALUE format


def Ask(b,h,g):  
  client_ID = client_id
  clientkey = clientKey
  passwod= pwdd
  user_agent= agent
  username= uname
  check_for_async=False
  reddit = praw.Reddit(
      client_id=client_ID,
      client_secret=clientkey,
      password=passwod,
      user_agent=user_agent,
      username=username,
      check_for_async=check_for_async,
  )
  a=reddit.subreddit(b)
  counter=0

  lis=[]
  comm=''
  if h=='new':
    b=a.new(limit=g)

    for i in b:

      if not i.stickied:

        title=i.title
        try:
          url_image=(i.preview['images'][0]['source']['url'])
        except:
          url_image="nothing"
        try:
          description=i.selftext
        except:
          description="nothing"
        try:
          video_link=i.media['reddit_video']['fallback_url']
        except:
          video_link=""
        com=i.comments
        counter=0
        for j in com:
          comm=j.body
          counter=counter+1
          if counter==1:
            break
        dic={"title":title,"url_image":url_image,"description":description,"video_link":video_link,"top_comment":comm}
        lis.append(dic)
        
    return lis
        
        
  if h=='hot':
    b=a.hot(limit=g)

    for i in b:

      if not i.stickied:
        title=i.title
        try:
          url_image=(i.preview['images'][0]['source']['url'])
        except:
          url_image="nothing"
        try:
          description=i.selftext
        except:
          description="nothing"
        try:
          video_link=i.media['reddit_video']['fallback_url']
        except:
          video_link=""
        com=i.comments
        counter=0
        for j in com:
          comm=j.body
          counter=counter+1
          if counter==1:
            break
        dic={"title":title,"url_image":url_image,"description":description,"video_link":video_link,"top_comment":comm}
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time inside function=", current_time)
        lis.append(dic)
        
    return lis
