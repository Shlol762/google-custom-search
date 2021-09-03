import requests
import aiohttp
import json
from .object import result

url="https://www.googleapis.com/customsearch/v1"

class ApiError(Exception):
  pass

class Engine_IdError(Exception):
  pass

class TokenError(Exception):
  pass

class custom_search(object): 
  def __init__(self, apikey=None, engine_id=None, image=False):
    if apikey is None:
      raise TokenError("apikey is invaid")
    if engine_id is None:
      raise Engine_IdError("engine_id is invaid")
    else: 
      self.token=apikey
      self.engine_id=engine_id
      self.image=image

  def search(self, keyword=None):
    if keyword is None:
      raise KeywordError("keyword is None")
    else:
      params={
        "key": self.token,
        "cx": self.engine_id,
        "q": keyword
      }
      res=requests.get(url,params=params)
      api=res.json()
      return result(api)
      
  async def search_async(self, keyword=None):
    if keyword is None:
      raise KeywordError("keyword is None")
    else:
      params={
        "key": self.token,
        "cx": self.engine_id,
        "q": keyword
      }
      async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as res:
          api=await res.json()
          return result(api)