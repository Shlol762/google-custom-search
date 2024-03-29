import json

class ImageError(Exception):
  pass


class ApiNotEnabled(Exception):
  def __init__(self, code: str, error: str):
    super().__init__(f"Error ({code}): {error}")


class result(object):
  def __init__(self, api, **kwarg):
    self.api: dict =api
    if self.api.get('error'):
      raise ApiNotEnabled(self.api['error']['code'], self.api['error']['message'])
    
  @property
  def titles(self):
    title=[]
    for e in self.api["items"]:
      i=e["title"]
      title.append(i)
    return title
    
  @property
  def urls(self):
    url=[]
    for e in self.api["items"]:
      i=e["link"]
      url.append(i)
    return url
    
  @property
  def display_urls(self):
    url=[]
    for e in self.api["items"]:
      i=e["displayLink"]
      url.append(i)
    return url
    
  @property
  def html_titles(self):
    title=[]
    for i in self.api["items"]:
      e=i["htmlTitle"]
      title.append(e)
    return title
    
  @property
  def snippets(self):
    snippet=[]
    for i in self.api["items"]:
      e=i["snippet"]
      snippet.append(e)
    return snippet
