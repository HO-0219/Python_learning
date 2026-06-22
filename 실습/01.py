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
