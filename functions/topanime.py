import os
import requests as req
def top():
  urls='https://api.jikan.moe/v3/anime/'+str(id)
  top='https://api.jikan.moe/v3/top/anime'
  data_top=req.get(top)
  data=req.get(urls)
  json=data.json()
  json_top=data_top.json()
  dict=[]
  dict_top=[]
  dict_top.append(json_top)
  top=dict_top[0]['top']
  a=""
  count=1
  for i in top:
    a=a+str(count)+':'+' '+i['title'] +'\n'
    count=count+1
    if count == 11:
      break
  return a