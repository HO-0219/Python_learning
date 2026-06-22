#비동기 
#여러 작업을 동시에 실행 가능
# async, await, asyncio 사용 
import asyncio

async def task(name, sec):
    print(f"{name} 시작...")
    await asyncio.sleep(sec)  # 비동기적으로 대기
    print(f"{name} 완료!")

async def main():
    await asyncio.gather(task("작업 1", 3), task("작업 2", 2))

asyncio.run(main())
