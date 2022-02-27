import json


class Item(object):
    def __init__(self, data, **kwargs):
        self.data: dict = data
    
    @property
    def title(self) -> str:
        return self.data["title"]
    
    @property
    def url(self) -> str:
        return self.data["link"]
    
    @property
    def display_url(self) -> str:
        return self.data["displayLink"]
    
    @property
    def html_title(self) -> str:
        return self.data["htmlTitle"]
    
    @property
    def snippet(self) -> str:
        return self.data["snippet"]
