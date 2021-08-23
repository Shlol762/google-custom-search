import google_custom_search
import os
import asyncio

google=google_custom_search.custom_search(apikey=os.getenv("token"), engine_id=os.getenv("engine_id"), image=True)

async def main():
  word=input("検索:")
  result=await google.search_async(word)
  for i in result.titles:
    print(i)
  for i in result.urls:
    print(i)
  for i in result.display_urls:
    print(i)
  for i in result.html_titles:
    print(i)
  for i in result.snippets:
    print(i)
    
while True:
  loop = asyncio.get_event_loop() 
  loop.run_until_complete(main())