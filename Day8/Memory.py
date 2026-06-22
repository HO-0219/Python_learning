# 메모리 최적화 !!! 

#__Slots__을 사용한 메모리 절약

class Person:
    __slots__ =['name','age'] 
    #name, age만 사용하여 메모리 사용 절약
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Python",55)
print(p.name, p.age)
#__dict__를 사용하지 않음으로 메모리 사용량이 줄어듦

# 제너레이터사용 메모리 절약 두둥탁!
def my_generator():
    for i in range(5):
        yield i #데이터를 한번에 메모리에 올리지 않음
    
gen = my_generator()
print(next(gen))
print(next(gen))
