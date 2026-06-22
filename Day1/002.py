"""함수 정의 방법"""
"""
def greet(name):
    print(f"heelow,{name}!")

greet("han")
greet(input("your name? "))

def add(a,b):
    return a+b

result = add(2,5)
print(f"result = {result}")
print(f"result = {add(4,10)}")
"""
""" List """
"""
numbers =[1,8,12,4,10]
for i in range(5):
    print(numbers[i])


print(numbers)
numbers.append(7)
numbers.remove(8)
print(numbers)
print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])
"""
"""튜블 tuple 변경 할 수 없는 자료형"""
"""
point= (10,20)
print(point[0])
print(point[1])
"""

"""dictionary 키와 값 구조의 데이터를 저장"""
"""
person = {"name" : "alice" , "age":25}
print(person["name"])
print(person.get("age"))
person["city"] = "seoul"
print(person)
print(person["city"])
"""
"""set  중복 허용 X 자료구조""""""
num = {1,2,3,3,5,6,7,2,2}
print(num)  
num.add(10)
num.remove(2)
print(num)"""
""" 반복 """"""
num = [1,2,3,4,5]
for n in range(len(num)):
    print(num[n])""""""
p ={"name" : "kim" , "age":22,"city":"seoul"}
for key,value in p.items():
    print(f"{key} : {value}")"""
""" 
TEST.1 이름과 나이를 입력받아 딕셔너리에 저장하고 출력
TEST.2 리스트를 받아서 모든 요소를 제곱한 새 리스트를 변환하는 함수
TEST.3 여러 숫자를 입력받아 중복을 제거한 후 정렬된 리스트로 반환
"""
"""TEST.1 이름과 나이를 입력받아 딕셔너리에 저장하고 출력
name = input("your name? ")
age = int(input("your age? "))
d = {"name": name , "age" : age}
print(f"your name : {d['name']} , your age : {d['age']} ")
"""
"""TEST.2 리스트를 받아서 모든 요소를 제곱한 새 리스트를 변환하는 함수""""""
def square(lst):
    squared_list = []
    for i in lst:
        squared_list.append(i * i)
    return squared_list

a = []
for i in range(10):
    a.append(int(input("Number? ")))

print("Original list:", a)
squared_a = square(a)  # 제곱된 리스트를 받음
print("Squared list:", squared_a)
    """
"""
TEST.3 여러 숫자를 입력받아 중복을 제거한 후 정렬된 리스트로 반환
"""

"""

a =[]
for i in range(4):
    a.append(int(input("number? ")))
a = sorted(set(a))
print(a)
"""

