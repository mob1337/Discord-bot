import os
import requests as req
def anime_quotes():
  api_res=req.get('https://animechan.vercel.app/api/random')
  api_data=api_res.json()
  quote=api_data['quote']
  anime=api_data['anime']
  char=api_data['character']
  return str(quote+" - "+char+" from "+anime)
