# google-custom-search

[![Downloads](https://pepy.tech/badge/google-custom-search)](https://pepy.tech/project/google-custom-search)
[![Downloads](https://pepy.tech/badge/google-custom-search/month)](https://pepy.tech/project/google-custom-search)
[![Downloads](https://pepy.tech/badge/google-custom-search/week)](https://pepy.tech/project/google-custom-search)
[![Documentation Status](https://readthedocs.org/projects/google-custom-search/badge/?version=latest)](https://google-custom-search.readthedocs.io/en/latest/?badge=latest)

# How to use this package.

## Next version can search image.

## first please install this package
```bash
pip install google-custom-search
```
or if you want use async/await, please install.
```bash
pip install google-custom-search[async]
```

## sample code
```py
import google_custom_search

google = google_custom_search.CustomSearch(apikey="your api_key", engine_id="your engine_id")
# if image is True, it's can search, but you need to setting at google console search

results = google.search("Hello")

for result in results:
    # get a title.
    print(result.title)
  
    # get a link.
    print(result.url)
  
    # get a displayLink.
    print(result.display_url)

    # get a htmlTitle.
    print(result.html_title)
  
    # get a snippet.
    print(result.snippet)
```

## sample code async version
```py
import asyncio
import google_custom_search

google = google_custom_search.CustomSearch(token="your api_key", engine_id="your engine_id", image=True)
# if image is True, it's can search, but you need to setting at google console search

async def main():
    results = await google.search_async("word!")
    for result in results:
        # get a title.
        print(result.title)
  
        # get a link.
        print(result.url)
  
        # get a displayLink.
        print(result.display_url)

        # get a htmlTitle.
        print(result.html_title)
  
        # get a snippet.
        print(result.snippet)
    
loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
```
