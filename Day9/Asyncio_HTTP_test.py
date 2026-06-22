#고성능 네트워크 프로그래밍!!!!!!

# 비동기 GET 요청
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = [
        "https://주소",
        "https://주소",
        "https://주소"
    ]

    tasks = [fetch(url) for url in urls]  # 여러 개의 요청 생성
    results = await asyncio.gather(*tasks)  # 동시에 실행

    for result in results:
        print(result)

asyncio.run(main())  # 비동기 실행
