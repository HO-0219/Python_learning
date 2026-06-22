""" 파일 입출력 
with open("Day-0/example.text","w") as file:
    file.write("hellow, wolrd \n")
    file.write("pythone file io is easy \n")

    

with open("Day-0/example.text","r") as file:
    content = file.read()

    print(content)
"""
""" 합,평균, 최대, 최소 값""""""
def list_operations(list):
    total = sum(list)
    average = total/len(list)
    max_value = max(list)
    min_value = min(list)
    return total,average,max_value,min_value

num = [1,3,4,5,6,8,9]
total, average,maxn,minn = list_operations(num)
print(f"Sum: {total}, Average: {average}, Max: {maxn}, Min: {minn}")
"""
"""
랜덤수 맞추기 게임
import random
def guess_number():
    target = random.randint(1,100)
    attempts = 0
    print("1~100 맞추기")

    while True:
        guess =int(input("your num? "))
        attempts += 1
        if guess < target:
            print(" 낮아요!")
        elif guess>target:
            print("높아요!")
        else:
            print(f"정답 : {guess}였습니다! {attempts}번 만에 맞췄어요!")
            break

guess_number()
"""

""" 팩토리얼 계산 
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("num"))
print(f"{num}의 팩토리얼은 {factorial(num)}이야")"""

""" 
TEST.1 사용자에게 파일이름을 받고 그 파일에 안녕 누구야 형식으로 인사말을 작성하는 프로그램을 작성


filename = input("file name?  ")
name = input("your name?  ")
with open(f"Day-0/{filename}.text","w")as file:
    file.write(f"안녕?! {name}아 반가워!")


TEST.2 주어진 숫자들의 합 평균 최대값 최소값을 구하느 프로그램 작성
a = []
for i in range(10):
    a.append(float(input("number :  ")))

def test(a):
    s = sum(a)
    av = s/len(a)
    m = max(a)
    mi = min(a)
    return s,av,m,mi

s,av,m,mi = test(a)
print(f"합계 : {s} , 평균 : {av}, 최대 값 : {m}, 최소값 : {mi}")

"""

"""
TEST.3 숫자 맞추기 게임 1~50 까지


import random
def ran():
    bat = random.randint(1,50)
    count = 0
    while True:
        num = int(input("number? "))
        count +=1

        if num > bat:
            print("num > bat")
        elif num<bat:
            print("num<bat")
        else:
            print("succes")
            break

ran()
"""

""" 
TEST.4 숫자 입력을 받아 해당 숫자의 팩토리얼 계산


num = int(input("number ?   " ))
def fac(n):
    if n ==1:
        return 1
    else:
        return n*fac(n-1)
print(f"{num}의 팩토리얼 은 {fac(num)}입니다")
    """