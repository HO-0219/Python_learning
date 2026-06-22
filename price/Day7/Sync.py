#동기프로그래밍
import time

def task(name, sec):
    print(f"{name} 시작...")
    time.sleep(sec)  # sec 초 동안 대기
    print(f"{name} 완료!")

task("작업 1", 3)
task("작업 2", 2)
