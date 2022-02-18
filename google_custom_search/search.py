import requests
import aiohttp
import json
from .object import result
from typing import Optional

url = "https://www.googleapis.com/customsearch/v1"

class ApiError(Exception):
    pass

class Engine_IdError(Exception):
    pass

class TokenError(Exception):
    pass

class custom_search(object): 
    def __init__(self,
                 apikey: str,
                 engine_id: str,
                 image: Optional[bool]=False):
        self.token = apikey
        self.engine_id = engine_id
        self.image = image

    def search(self, keyword:str) -> result:
        params={
            "key": self.token,
            "cx": self.engine_id,
            "q": keyword
        }
        res = requests.get(url,params=params)
        return result(res.json())
      
    async def search_async(self, keyword:str) -> result:
        params={
            "key": self.token,
            "cx": self.engine_id,
            "q": keyword
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as res:
                return result(await res.json())
