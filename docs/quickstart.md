# Quick start

## install

```bash
pip install google-custom-search```

## sample

### sync

```py
import google_custom_search
google = google_custom_search.custom_search(apikey="your api_key", engine_id="your engine_id")
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

### async

```py
import asyncio
import google_custom_search
google = google_custom_search.custom_search(token="your api_key", engine_id="your engine_id", image=True)
# if image is True, it's can search, but you need to setting at google console search
async def main():
    result = await google.search_async("word!")
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