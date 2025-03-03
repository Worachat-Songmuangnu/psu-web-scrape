import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime

async def fetch(session, url):
    async with session.get(url) as response: 
        return await response.text()

async def scrape(url):
    start_time = datetime.now()

    async with aiohttp.ClientSession() as session:  
        html = await fetch(session, url) 
        soup = BeautifulSoup(html, 'html.parser') 
        title = soup.title.text  

    end_time = datetime.now()
    print(f"Title: {title}")
    print(f"Time taken: {end_time - start_time} \n") 

async def main():
    urls = [
        "https://www.psu.ac.th/",
        "https://www.eng.psu.ac.th/",
        "https://www.coe.psu.ac.th/"
    ]
    tasks = [scrape(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())
