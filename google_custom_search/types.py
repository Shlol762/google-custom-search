import json


class Item(object):
    """This is return a item."""
    def __init__(self, data, **kwargs):
        self.data: dict = data
    
    @property
    def title(self) -> str:
        """This is the title of the item."""
        return self.data["title"]
    
    @property
    def url(self) -> str:
        """This is the url of the item."""
        return self.data["link"]
    
    @property
    def display_url(self) -> str:
        """This is the display url of the item."""
        return self.data["displayLink"]
    
    @property
    def html_title(self) -> str:
        """This is the html title of the item."""
        return self.data["htmlTitle"]
    
    @property
    def snippet(self) -> str:
        """This is the snippet of the item."""
        return self.data["snippet"]
