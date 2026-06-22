#데코레이서 코드 
def decorator(func):
    def wrapper():
        print("함수 실행전")
        func()
        print("함수 실행 후")
    return wrapper

@decorator
def hello():
    print("hello? python?")

hello()

# N개의 데코레이터 사용
def upperacse_decorator(func):
    def wrapper():
        result =func()
        return result.upper()   #대문자로 변환
    return wrapper
@upperacse_decorator
def greet():
    return "hellow"
print(greet())

# 데코레이터 인자 전달
def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator
@repeat(3)
def say_hello():
    print("Hello")
say_hello()