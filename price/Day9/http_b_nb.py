# 동기, 비동기 예제 

#동기 방식 requstes
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())  # JSON 응답 출력

# 비동기 방식 aiohttp
import aiohttp
import asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            print(await response.json())

asyncio.run(fetch())
