import json


class Item(object):
    def __init__(self, data, **kwargs):
        self.data: dict = data
    
    @property
    def title(self):
        return self.data["title"]
    
    @property
    def url(self):
        return self.data["link"]
    
    @property
    def display_url(self):
        return self.data["displayLink"]
    
    @property
    def html_title(self):
        return self.data["htmlTitle"]
    
    @property
    def snippet(self):
        return self.data["snippet"]
