"""

a= 10
b= 15
print(a,b)
c= a+b
print(c)
print(a+b)
text = "hellow pytohn! ?"
print(text)
is_bool =True
print(is_bool)
name = "alice"
age = 24
print("name :",name," age : ", age)
"""
"""
input 

name_input = input("your name? " )
age_input = input("your age? ")
print("name :", name_input, "age :",age_input)
"""
"""
age = int(input("your age ?"))
if age>=18:
    print("your are adult")
else:
    print("your no adult ")
"""
"""
i = 0 ~ 4 까지 반복
for i in range(5):
    print(i)
"""
"""

index = 0
while index < 5:
    print(index)
    index+=1
"""
"""
Test.1 값을 입력받아 출력하기 
Test.2 숫자를 입력받아 홀짝 구분
Test.3 1~10의 합을 구하기
"""
"""Test.1 값을 입력받아 출력하기 """
"""
age = int(input("your age?  "))
name = input("your name?  ")
if age >= 18 :
    print("your name is ",name , "your age is ", age , "your adult! ")
elif age >= 8:
    print("your name is ",name , "your age is ", age , "your student! ")
else:
    print(f"Your name is {name}, your age is {age}, you are a child!")
    
"""

"""Test.2 숫자를 입력받아 홀짝 구분"""
"""
num = int(input("number ?"))
print("짝수"if num % 2 ==0 else "홀수")
"""

"""Test.3 1~10의 합을 구하기"""
"""
count = 1
sum =0
while count<=10:
    sum = sum +count
    count = count +1
    
print(sum)
"""







