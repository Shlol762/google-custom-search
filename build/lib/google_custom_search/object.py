import json

class ImageError(Exception):
  pass

class result(object):
  def __init__(self, api, **kwarg):
    self.api=api
    
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