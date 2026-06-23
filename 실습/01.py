# print(" ----------------------------")
# print(" ---------- 28번 문제 ---------")
# print(" ----------------------------")
# pay = int(input("급여 입력 : " ) )  


# if pay >= 500:
#     year = pay*12
# else:
#     year = pay*13

# if year < 1000:
#     duty = 0
# elif 1000 <= year < 5000:
#     duty = year * 0.10
# elif 5000 <= year < 7000:
#     duty = year * 0.12
# elif 7000 <= year < 10000:
#     duty = year * 0.15
# else :
#     duty = year * 0.2

# print("급여 :  %d "% pay)
# print("연봉 : %d " % year)
# print("세금 : %0.2f "% duty)


# print(" ----------------------------")
# print(" ---------- 31번 문제 ---------")
# print(" ----------------------------")

# num = int(input("숫자 입력 : "))
# sum = 0
# if num < 0:
#     num= num *-1
#     print("음수여서 n * -1 진행 (ABS 로 가능 함 )")

# nam = num
# while num != 0 :
#     sum = sum + num
#     num = num -1

# print("1 ~ %d 까지 합 : %d" % (nam,sum))

# num1 =int(input("숫자 1번 입력 : "))
# # 1  or 11 
# nam1 =int(input("숫자 2번 입력 : "))
# # 11 or 1 
# # 1 > 11 
# sum1 =0

# if num1 > nam1:
#     num1,nam1 = nam1, num1

# nn = num1
# while nam1 >= num1 :
#     sum1 = sum1 + num1
#     num1 = num1 +1 


# print("%d ~ %d 까지의 합 : %d " % (nn, num1-1, sum1)) 



# print(" ----------------------------")
# print(" ---------- 33번 문제 ---------")
# print(" ----------------------------")


# i = 0 
# e = 0  #짝
# a = 0  # 홀 
# while i < 10:
#     i = i +1
#     if i %2 ==0 : 
#         e = e+i
#     else :
#         a = a+i

# print ("짝수의 합은 : %d "% e)
# print ("홀수의 합은 : %d "%a)




# print(" ----------------------------")
# print(" ---------- 36번 문제 ---------")
# print(" ----------------------------")
# coffee = int(input("재고 갯수 입력 : "))
# price = int(input("단가 입력 "))

# print (" 카페 %d 개의 커피를 다 팔아야함 가격은 %d " % (coffee, price))
# while True:
#     print("남은거 %d" % (coffee))
#     pay = int(input(" 돈 내놔  : " ))
#     if pay >= price:
#         coffee = coffee -1 
#         pay = pay - price
#         print(" 쓰레기 한개 판매 ")
#         print(" 거스름 돈 : %d " % pay)
#     else :
#         print(" 돈 없으면 꺼지쇼 ")

#     if coffee == 0 :
#         break
    
# print(" ----------------------------")
# print(" ---------- 53번 문제 ---------")
# print(" ----------------------------")

# man = [90, 30, 65, 45 ,85]
# print(" ----------------------------")
# print( " 응시자별 점수 ")
# print(" ----------------------------")
# for i in range(0, len(man)):
#     if man[i] >= 60:
#         print("%d번째 응시자는 %d : 합격" % ((i+1),man[i]))
#     else:
#         print("%d번째 응시자는 %d : 불합격" % ((i+1),man[i]))


# print(" ----------------------------")
# print( " 합격자만")
# print(" ----------------------------")    
# count =1 
# for i in man:
#     if i >= 60:
#         print("%d번째 응시자는 %d : 합격" % (count,i))
#     count+=1
    
# print(" ----------------------------")
# print(" ---------- 53번 문제 ---------")
# print(" ----------------------------")

# l = "life is an egg"
# l = l.split()
# print(type(l))

# print( "Before list : %s " % l)

# for i in range(len(l)):
#     if i%2 == 0:
#         l[i] = l[i].upper()
#     else:
#         l[i] = l[i].lower()
        

# print( "After list : %s " % l)
# j = '#'.join(l)
# print(j)

# print(" ----------------------------")
# print(" ---------- 46번 문제 ---------")
# print(" ----------------------------")

# bread = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
# # 0 , 3, 6 
# bread = bread.split(',')
# print('-'*10)
# print(bread)
# print('-'*10)
# # br = bread[1:2]
# # print('-'*10)
# # print(br)
# # print('-'*10)
# br=[]

# for i in range(len(bread)):
#     if i %3 ==0:
#         print('-'*10)
#         print(bread[i])
#         br.append(bread[i])
#         print('-'*10)

# br.append(bread[1])
# print(br)



# print(" ----------------------------")
# print(" ---------- 48번 문제 ---------")
# print(" ----------------------------")

# bread = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
# breadlist = bread.split(',')
# print('-'*10)
# print(bread)
# print('-'*10)


# tbread = tuple(bread.split(','))
# print('-'*10)
# print(tbread)
# print('-'*10)

# c = breadlist.count('스콘')
# print('-'*10)
# print("스콘의 갯수는 %d" % c)
# print('-'*10)
# a = breadlist.index('스콘')
# print('-'*10)
# print (a) 
# print('-'*10)
# re = breadlist[:3] + breadlist[-3:]
# print('-'*10)
# print(re)
# print('-'*10)

# sorted_bread = sorted(re)
# print('-'*10)
# print(sorted_bread)
# print('-'*10)

print(" ----------------------------")
print(" ---------- 문자열 함수 총 정리---------")
print(" ----------------------------")

# 문자열 기본 예제
# 아래 예제들은 실행 결과를 print 하지 않고, 오른쪽 주석에 결과를 적어둔 공부용 정리입니다.
s = "  Python String Test  "
text = "apple,banana,apple,orange"
num = "12345"
kor = "바게트,크로와상,스콘"

# 1. 대소문자 변환
# 영어 문자열을 검색/비교할 때 대소문자를 맞추기 위해 자주 사용합니다.
# 예: "Python"과 "python"을 같은 단어로 보고 싶으면 둘 다 lower() 처리
s.lower()                 # '  python string test  ' 소문자 처리 
s.upper()                 # '  PYTHON STRING TEST  ' 대문자로 
s.capitalize()            # '  python string test  ' 첫글자만 대문자 나머지 소문자
"python string".title()    # 'Python String' 각단어 첫글자만 대문자
"PyThOn".swapcase()        # 'pYtHoN' 반전
"Straße".casefold()        # 'strasse' / lower()보다 강한 소문자 변환

# 2. 공백 제거
# 사용자 입력값, 파일 데이터, 웹 요청 데이터 앞뒤에 붙은 불필요한 공백을 제거할 때 씁니다.
# strip()은 양쪽, lstrip()은 왼쪽, rstrip()은 오른쪽만 제거합니다.
s.strip()                 # 'Python String Test' 불필요한 양쪽 공백 제거
s.lstrip()                # 'Python String Test  ' 불필요한 왼쪽 공백 제거
s.rstrip()                # '  Python String Test' 불필요한 오른쪽 공백 제거
"---hello---".strip("-")   # 'hello' 양쪽 '-' 제거 
"---hello---".lstrip("-")  # 'hello---' 왼쪽 '-' 제거
"---hello---".rstrip("-")  # '---hello' 오른쪽 '-'제거 

# 3. 찾기
# 문자열 안에 특정 "글자" 가 어디 있는지 찾습니다.
# find()는 없으면 -1, index()는 없으면 에러가 나므로 상황에 따라 선택합니다.
text.find("banana")        # 6 / 찾으면 시작 인덱스 
text.find("melon")         # -1 / 없으면 -1
text.rfind("apple")        # 13 / 오른쪽부터 찾은 위치 오
text.index("banana")       # 6 / find와 비슷하지만 없으면 에러
text.rindex("apple")       # 13 / 오른쪽부터 찾고 없으면 에러
"스콘" in kor              # True  문자열 안에 들어 있는지 여부 
"식빵" in kor              # False

# 4. 개수 세기
# 문자열 안에 특정 글자나 단어가 몇 번 나오는지 셉니다.
# 검색어 등장 횟수, 특정 구분자 개수 확인 등에 사용할 수 있습니다.
text.count("apple")        # 2
text.count("a")            # 5
kor.count("스콘")          # 1

# 5. 시작/끝 확인
# 파일 확장자, URL, 접두어, 접미어를 검사할 때 많이 씁니다.
# endswith()에는 여러 후보를 튜플로 넣을 수도 있습니다.
text.startswith("apple")   # True 시작
text.endswith("orange")    # True 끝 
"hello.py".endswith(".py")  # True 끝에 ".py"가 붙어 있냐
"image.png".endswith((".jpg", ".png"))  # True 끝에 ".jpg" 또는 ".png"가 붙어 있는지

# 6. 바꾸기
# 문자열의 특정 부분을 다른 문자열로 바꿉니다.
# 전화번호 하이픈 제거, 금지어 치환, 단어 교체 등에 사용합니다.
text.replace("apple", "kiwi")      # 'kiwi,banana,kiwi,orange' (바꿀단어, 바꾸는단어)
text.replace("apple", "kiwi", 1)   # 'kiwi,banana,apple,orange' (바꿀단어, 바꾸는단어, 갯수)
"010-1234-5678".replace("-", "")   # '01012345678' "-"를 ""제거한다

# 7. 나누기
# 문자열을 리스트로 쪼갭니다.
# CSV, 태그, 검색어, 입력값처럼 구분자가 있는 데이터를 처리할 때 핵심입니다.
text.split(",")             # ['apple', 'banana', 'apple', 'orange']
"a b c".split()             # ['a', 'b', 'c'] / 공백 기준
"a,b,c,d".split(",", 2)     # ['a', 'b', 'c,d']
"a,b,c,d".rsplit(",", 2)    # ['a,b', 'c', 'd']
"line1\nline2".splitlines() # ['line1', 'line2']

# 8. 합치기
# 리스트에 들어있는 문자열들을 하나의 문자열로 합칩니다.
# split()의 반대 느낌이고, 결과 출력이나 CSV 형태 만들 때 자주 씁니다.
",".join(["a", "b", "c"])   # 'a,b,c'
" ".join(["hello", "python"])  # 'hello python'
"".join(["1", "2", "3"])    # '123'

# 9. 분리하기
# split()처럼 전부 쪼개지 않고, 기준 문자열을 중심으로 딱 3부분으로 나눕니다.
# 이메일, 파일 경로, URL 같은 값을 앞/기준/뒤로 나눌 때 유용합니다.
"user@example.com".partition("@")   # ('user', '@', 'example.com')
"a/b/c".rpartition("/")             # ('a/b', '/', 'c')
"abc".partition("@")                # ('abc', '', '')

# 10. 정렬/채우기
# 문자열 길이를 맞춰서 출력 모양을 정리할 때 씁니다.
# 번호표, 금액, 표 형태 출력처럼 자리수를 맞춰야 할 때 유용합니다.
"python".center(10)         # '  python  '
"python".center(10, "-")    # '--python--'
"python".ljust(10, ".")     # 'python....'
"python".rjust(10, ".")     # '....python'
"42".zfill(5)               # '00042'
"-42".zfill(5)              # '-0042'

# 11. 문자 종류 확인
# 문자열이 숫자인지, 알파벳인지, 공백인지 등을 True/False로 확인합니다.
# 입력값 검증에 많이 사용합니다. 예: 나이 입력값이 숫자인지 확인
"abc123".isalnum()          # True / 문자 또는 숫자
"abc".isalpha()             # True / 문자
"123".isdigit()             # True / 숫자
"123".isdecimal()           # True / 십진수 숫자
"123".isnumeric()           # True / 숫자 표현
"hello".islower()           # True
"HELLO".isupper()           # True
"Hello Python".istitle()    # True
"   ".isspace()             # True
"name_1".isidentifier()     # True / 변수명으로 사용 가능
"hello".isascii()           # True
"안녕".isascii()            # False
"hello\n".isprintable()     # False

# 12. 접두사/접미사 제거
# 문자열 앞이나 뒤에 특정 문자열이 있을 때만 제거합니다.
# replace()와 달리 중간에 있는 글자는 건드리지 않습니다.
"unhappy".removeprefix("un")        # 'happy'
"report.pdf".removesuffix(".pdf")   # 'report'
"unhappy".removeprefix("pre")       # 'unhappy' / 없으면 원본 유지

# 13. 탭/인코딩/변환
# 탭 간격을 바꾸거나, 문자열을 바이트로 인코딩하거나, 문자 단위 변환표를 만들 때 씁니다.
# encode()는 파일 저장, 네트워크 전송, API 처리에서 볼 수 있습니다.
"a\tb".expandtabs(4)        # 'a   b'
"hello".encode("utf-8")     # b'hello'
str.maketrans("abc", "123") # {97: 49, 98: 50, 99: 51}
"abc".translate(str.maketrans("abc", "123"))  # '123'

# 14. 문자열 포맷팅
# 변수 값을 문자열 안에 끼워 넣을 때 사용합니다.
# 요즘은 f-string을 가장 많이 씁니다.
"{} loves {}".format("Tom", "Python")          # 'Tom loves Python'
"{name} loves {lang}".format(name="Tom", lang="Python")  # 'Tom loves Python'
"{name} loves {lang}".format_map({"name": "Tom", "lang": "Python"})  # 'Tom loves Python'
name = "Tom"
lang = "Python"
f"{name} loves {lang}"       # 'Tom loves Python'

# 15. 인덱싱/슬라이싱/길이
# 문자열도 리스트처럼 위치 번호로 접근할 수 있습니다.
# 슬라이싱은 일부 글자만 잘라낼 때 사용합니다.
"python"[0]                  # 'p'
"python"[-1]                 # 'n'
"python"[0:2]                # 'py'
"python"[:3]                 # 'pyt'
"python"[3:]                 # 'hon'
"python"[::2]                # 'pto'
"python"[::-1]               # 'nohtyp'
len("python")                # 6

# 16. 문자열 비교/정렬에 자주 쓰는 함수
# 문자열 정렬은 기본적으로 유니코드 순서를 따릅니다.
# 대소문자를 무시하고 정렬하고 싶으면 key=str.lower 같은 기준을 줄 수 있습니다.
sorted(["banana", "apple", "orange"])  # ['apple', 'banana', 'orange']
sorted(["b", "A", "a"])                # ['A', 'a', 'b'] / 유니코드 순서
sorted(["b", "A", "a"], key=str.lower) # ['A', 'a', 'b'] / 대소문자 무시 느낌




print(" ----------------------------")
print(" ---------- list 함수 총 정리---------")
print(" ----------------------------")

# 리스트는 여러 값을 순서대로 저장하고, 값을 추가/삭제/수정할 수 있습니다.
# append(), extend(), insert(), remove(), pop(), sort(), reverse()를 가장 많이 씁니다.
nums = [3, 1, 4, 1, 5]
words = ["apple", "banana", "orange"]

# 1. 추가
nums.append(9)              # [3, 1, 4, 1, 5, 9] / 맨 뒤에 1개 추가
nums.extend([2, 6])         # [3, 1, 4, 1, 5, 9, 2, 6] / 여러 개 추가
nums.insert(1, 100)         # [3, 100, 1, 4, 1, 5, 9, 2, 6] / 원하는 위치에 추가

# 2. 삭제
nums.remove(1)              # 첫 번째 1 삭제 / 없으면 에러
nums.pop()                  # 맨 뒤 값 삭제하고 반환
nums.pop(0)                 # 0번 인덱스 값 삭제하고 반환
del nums[0]                 # 0번 인덱스 값 삭제
words.clear()               # [] / 전체 삭제

# 3. 찾기/개수
nums = [3, 1, 4, 1, 5]
nums.index(4)               # 2 / 값 4의 위치
nums.count(1)               # 2 / 값 1의 개수
1 in nums                   # True
9 not in nums               # True

# 4. 정렬/뒤집기
nums.sort()                 # [1, 1, 3, 4, 5] / 원본 변경
nums.sort(reverse=True)     # [5, 4, 3, 1, 1] / 내림차순
sorted(nums)                # [1, 1, 3, 4, 5] / 새 리스트 반환
nums.reverse()              # 원본 순서 뒤집기
list(reversed(nums))        # 뒤집은 새 리스트 느낌

# 5. 복사/슬라이싱
a = [1, 2, 3]
b = a                       # 같은 리스트를 같이 바라봄
c = a.copy()                # 새 리스트로 얕은 복사
d = a[:]                    # 새 리스트로 얕은 복사
a[0] = 100                  # b도 같이 바뀌고, c와 d는 유지
a[0]                        # 100
b[0]                        # 100
c[0]                        # 1

# 6. 자주 쓰는 기본 함수
len([1, 2, 3])              # 3
sum([1, 2, 3])              # 6
max([1, 2, 3])              # 3
min([1, 2, 3])              # 1
list("abc")                 # ['a', 'b', 'c']

# 7. 리스트 컴프리헨션
# 반복문으로 새 리스트를 만들 때 간단하게 씁니다.
[i for i in range(5)]       # [0, 1, 2, 3, 4]
[i * 2 for i in range(5)]   # [0, 2, 4, 6, 8]
[i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]


print(" ----------------------------")
print(" ---------- tuple 함수 총 정리---------")
print(" ----------------------------")

# 튜플은 리스트처럼 순서가 있지만, 한 번 만들면 값을 바꿀 수 없습니다.
# 그래서 append(), remove(), sort() 같은 수정 메서드는 없습니다.
t = (10, 20, 30, 20)

t.count(20)                 # 2 / 값 20의 개수
t.index(30)                 # 2 / 값 30의 위치
len(t)                      # 4
20 in t                     # True
t[0]                        # 10
t[-1]                       # 20
t[1:3]                      # (20, 30)

# 튜플 만들기
one = (1,)                  # 값 1개짜리 튜플은 쉼표 필요
not_tuple = (1)             # int / 튜플 아님
tuple([1, 2, 3])            # (1, 2, 3)
list((1, 2, 3))             # [1, 2, 3]

# 튜플 언패킹
x, y = (10, 20)
x                            # 10
y                            # 20


print(" ----------------------------")
print(" ---------- dict 함수 총 정리---------")
print(" ----------------------------")

# 딕셔너리는 key와 value를 묶어서 저장합니다.
# key로 빠르게 값을 찾을 수 있어서 회원정보, 점수표, 카운팅에 자주 사용합니다.
student = {"name": "Tom", "age": 20, "score": 90}

# 1. 조회
student["name"]             # 'Tom' / key가 없으면 에러
student.get("name")         # 'Tom'
student.get("grade")        # None / key가 없어도 에러 안 남
student.get("grade", "A")   # 'A' / 기본값 지정
"name" in student           # True / key 존재 여부

# 2. 추가/수정
student["age"] = 21         # 기존 key면 수정
student["grade"] = "A"      # 없는 key면 추가
student.update({"score": 95, "city": "Seoul"})  # 여러 개 추가/수정

# 3. 삭제
student.pop("city")         # key 삭제하고 value 반환
student.pop("none", "없음") # key 없을 때 기본값 반환
student.popitem()           # 마지막 key-value 삭제하고 반환
student["grade"] = "A"      # del 예제를 위해 다시 추가
del student["grade"]        # key 삭제 / 없으면 에러

# 4. key/value/item 꺼내기
student.keys()              # dict_keys(['name', 'age', 'score'])
student.values()            # dict_values(['Tom', 21, 95])
student.items()             # dict_items([('name', 'Tom'), ('age', 21), ('score', 95)])
list(student.keys())        # ['name', 'age', 'score']

# 5. 반복문
for key in student:
    key                      # key가 하나씩 나옴

for key, value in student.items():
    key, value               # key와 value가 같이 나옴

# 6. 기본값 세팅
counts = {}
counts.setdefault("apple", 0)  # apple이 없으면 0으로 만들고 반환
counts["apple"] += 1           # {'apple': 1}

# 7. 딕셔너리 컴프리헨션
{i: i * i for i in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


print(" ----------------------------")
print(" ---------- set 함수 총 정리---------")
print(" ----------------------------")

# set은 중복을 허용하지 않고, 순서가 없습니다.
# 중복 제거, 교집합/합집합/차집합 계산에 많이 씁니다.
s1 = {1, 2, 3, 3}
s2 = {3, 4, 5}

s1                           # {1, 2, 3}
set([1, 1, 2, 2, 3])         # {1, 2, 3}
s1.add(4)                    # 값 4 추가
s1.update([5, 6])            # 여러 값 추가
s1.remove(6)                 # 값 삭제 / 없으면 에러
s1.discard(100)              # 값 삭제 / 없어도 에러 안 남
s1.pop()                     # 아무 값 하나 삭제하고 반환

s1 | s2                      # 합집합
s1 & s2                      # 교집합
s1 - s2                      # 차집합
s1 ^ s2                      # 대칭 차집합
s1.union(s2)                 # 합집합
s1.intersection(s2)          # 교집합
s1.difference(s2)            # 차집합


print(" ----------------------------")
print(" ---------- Stack 스택 정리---------")
print(" ----------------------------")

# 스택은 마지막에 넣은 값이 먼저 나오는 구조입니다. LIFO라고 부릅니다.
# 파이썬에서는 보통 list의 append(), pop()으로 구현합니다.
stack = []
stack.append("A")            # push / 넣기
stack.append("B")
stack.append("C")
stack.pop()                  # 'C' / 마지막 값 꺼내기
stack[-1]                    # 가장 위 값 확인
len(stack) == 0              # 비어 있는지 확인

# 사용 예: 되돌리기, 괄호 검사, DFS


print(" ----------------------------")
print(" ---------- Queue 큐 정리---------")
print(" ----------------------------")

# 큐는 먼저 넣은 값이 먼저 나오는 구조입니다. FIFO라고 부릅니다.
# list.pop(0)은 느릴 수 있어서 collections.deque를 많이 씁니다.
from collections import deque

queue = deque()
queue.append("A")            # enqueue / 뒤에 넣기
queue.append("B")
queue.append("C")
queue.popleft()              # 'A' / 앞에서 꺼내기
queue[0]                     # 가장 앞 값 확인
len(queue) == 0              # 비어 있는지 확인

# 양쪽에서 넣고 빼기
dq = deque([1, 2, 3])
dq.appendleft(0)             # 왼쪽에 추가
dq.append(4)                 # 오른쪽에 추가
dq.popleft()                 # 왼쪽에서 꺼내기
dq.pop()                     # 오른쪽에서 꺼내기


print(" ----------------------------")
print(" ---------- heapq 힙 정리---------")
print(" ----------------------------")

# heapq는 항상 가장 작은 값이 먼저 나오는 최소 힙입니다.
# 우선순위 큐를 만들 때 많이 씁니다.
import heapq

heap = []
heapq.heappush(heap, 5)      # 값 추가
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heap[0]                      # 1 / 가장 작은 값 확인
heapq.heappop(heap)          # 1 / 가장 작은 값 꺼내기

# 기존 리스트를 힙으로 바꾸기
heap2 = [5, 1, 3, 2]
heapq.heapify(heap2)         # 리스트를 힙 구조로 변경
heapq.heappop(heap2)         # 1

# 가장 큰 값부터 꺼내고 싶으면 음수로 넣는 방법을 많이 씁니다.
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)
-heapq.heappop(max_heap)     # 5

# 자주 쓰는 함수
heapq.nsmallest(2, [5, 1, 3, 2])  # [1, 2]
heapq.nlargest(2, [5, 1, 3, 2])   # [5, 3]


print(" ----------------------------")
print(" ---------- Hash Table 해시 테이블 정리---------")
print(" ----------------------------")

# 해시 테이블은 key를 해시값으로 바꿔서 빠르게 찾는 자료구조입니다.
# 파이썬의 dict와 set이 해시 테이블 기반입니다.
# 평균적으로 검색/추가/삭제가 빠릅니다.
phone_book = {}
phone_book["Tom"] = "010-1111-2222"    # 추가
phone_book["Jane"] = "010-3333-4444"
phone_book["Tom"]                       # key로 빠르게 조회
"Jane" in phone_book                    # key 존재 확인
phone_book.pop("Jane")                  # 삭제

# 해시 테이블로 개수 세기
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = {}
for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
fruit_count                              # {'apple': 3, 'banana': 2, 'orange': 1}

# collections.Counter를 쓰면 더 간단합니다.
from collections import Counter

Counter(fruits)                          # Counter({'apple': 3, 'banana': 2, 'orange': 1})


print(" ----------------------------")
print(" ---------- 자료구조 선택 정리---------")
print(" ----------------------------")

# list  : 순서가 중요하고, 값 수정/추가/삭제가 필요할 때
# tuple : 순서가 중요하지만, 값이 바뀌면 안 될 때
# dict  : key로 value를 빠르게 찾고 싶을 때
# set   : 중복 제거, 포함 여부 확인, 집합 연산이 필요할 때
# stack : 마지막에 넣은 값을 먼저 처리할 때
# queue : 먼저 넣은 값을 먼저 처리할 때
# heapq : 가장 작은 값 또는 우선순위가 높은 값을 먼저 처리할 때
# hash table : key 기반 빠른 검색/추가/삭제가 필요할 때(dict, set)
