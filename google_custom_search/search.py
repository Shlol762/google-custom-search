import requests
try:
    import aiohttp
except:
    no_async = True
else:
    no_async = False
    
from typing import Optional, List
from .errors import ApiNotEnabled, AsyncError
from .types import Item

class custom_search(object):
    APIURL = "https://www.googleapis.com/customsearch/v1"
    
    def __init__(self,
                 apikey: str,
                 engine_id: str,
                 image: Optional[bool]=False):
        self.token = apikey
        self.engine_id = engine_id
        self.image = image

    def search(self, keyword: str) -> List[Item]:
        params={
            "key": self.token,
            "cx": self.engine_id,
            "q": keyword
        }
        res = requests.get(self.APIURL, params=params)
        return self._from_dict(res.json())
    
    def _from_dict(self, data) -> List[Item]:
        if data.get('error'):
            raise ApiNotEnabled(self.api['error']['code'], self.api['error']['message'])
        else:
            return [Item(i) for i in data["items"]]
      
    async def search_async(self, keyword: str) -> List[Item]:
        if no_async:
            raise AsyncError("This library can't use aiohttp. Please install aiohttp")
        params={
            "key": self.token,
            "cx": self.engine_id,
            "q": keyword
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.APIURL, params=params) as res:
                return self._from_dict(await res.json())
