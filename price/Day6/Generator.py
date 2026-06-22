#제너레이터 

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# yield는 값을 반환하지만 함수 실행을 멈추지 않고 다음 실행을 기다림

# 제너레이터로 무한 수열 생성
def infinite_sequence():
    num = 0
    while True:
        yield num  
        num+=1
gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#메모리를 적게 사용하며 무한 루프 가능
print("----=-=-=-=-=-=-=-=-=-=-")
# 제네레이터 표현식
# 리스트 컴프리헨션 처럼 간결하게 제너레이터를 만들 수 있음
gen_exp =(x**2 for x in range(5))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))

