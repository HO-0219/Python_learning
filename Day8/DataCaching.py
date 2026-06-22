#데이터 캐싕

# lru_cache를 사용한 캐싱

from functools import lru_cache
import time

@lru_cache(maxsize=5) #최근 5개의 결과 캐싱
def show_function(n):
    time.sleep(3) # 3초 연산 시간 가장
    return n*n
print(show_function(3))  # 처음 호출 - 3초
print(show_function(3)) # 즉시 
print(show_function(2)) #2는 처음이 이기에 연산시간 걸림 
print(show_function(3)) # 즉시 


