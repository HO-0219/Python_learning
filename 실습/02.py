# print("-"*40)
# print(" ---------- 60 중첩 리스트---------")
# print("-"*40)

# # 이름, 주민번호, 국어, 영어
# kim = ['김현숙', '801225-2234567', 60, 80]
# lee = ['이민혁', '901111-1027890', 90, 100]
# park = ['박춘섭', '000717-3123456', 40, 90]
# choi = ['최영희', '100815-4123456', 70, 80]
# ha = ['하수빈', '730815-2123456', 30, 70]

# st = list()
# st.append(kim)
# st.append(lee)
# st.append(park)
# st.append(choi)
# st.append(ha)
# print("-"*10)
# print( st )
# print("-"*10)
# ss = st[1][1]
# print("-"*10)
# print(ss)
# print("-"*10)
# st[0][3] = 70
# print("-"*10)
# print (st)
# print("-"*10)

# for bean in st:
#     print("-"*10)
#     name =bean[0]
#     ssn = bean[1]
#     kor = bean[2]
#     eng = bean[3]
#     year = int(ssn[0:2])

#     if year >= 27 :
#         br = year + 1900
#     else:
#         br = year+2000
    
#     br = 2026 - br 
    
#     if ssn[7:8] == '2' or ssn[7:8] == '4' :
#         gender = '여성' 
#     else:
#         gender ='남성'

#     if br >= 40 :
#         tt = '중년'
#     elif br >=20 :
#         tt ='청년'
#     else :
#         tt= '미성년'
    
#     to = int(kor + eng )
#     avg = float(to /2.0)
#     if avg >= 90.0 :
#         g = 'A'
#     elif avg>=80.0 :
#         g ='B'
#     elif avg>=70.0:
#         g='C'
#     elif avg>=60.0:
#         g ='D'
#     else:
#         g='F'    
#     print(name , ssn , year, br, tt, gender, to,avg,g)
#     print("-"*10)

    
# print("-"*40)
# print(" ---------- 리스트 컴프리 핸션 ---------")
# print("-"*40)

# print("-"*10)

# s = [ x ** 2 for x in range(1,6)]
# print(s)
# print("-"*10)

# s = [ x for x in range(1,101,3)]
# print (s)
# print("-"*10)

# s = [ x for x in range(1 ,101,3 ) if x %10 ==0 ]
# print (s)
# print("-"*10)

# e = [75,30,85,50]
# s = [ x for x in e if x>=60 ]
# print ("합격한 사람 %d 명 " % len(s))
# print("-"*10)

# s = [ x for x in range(1 ,10)]
# print (s)
# print("-"*10)

   
# print("-"*40)
# print(" ---------- 50번 문제  ---------")
# print("-"*40)
# # 초기데이터 바게트 :100 치아바타:200 호밀빵:300 , 베이글:400
# b ={'바게트': 100, '치아바타': 200, '호밀빵': 300, '베이글': 400}
# # 스콘이 존재 하지 않으면 150원 으로 추가 
# if  "스콘" not in b :
#     b["스콘"] = 150      # 없는 key면 추가


# # 치아바타 가격을 250원으로 수정 
# b['치아바타'] = 250
# # 단가 300원짜리가 존재 하는지 체크 후 없으면 300원으로 브리오슈 추가 
# c = 0
# for key in b :
#     if b[key] >= 300:
#         c=c+1
    
# if c !=0 :
#     b["브리오슈"] = 300


# # 리스트 반복문을 통해 통밀빵, 옥수수 빵, 크렌베리빵 을 추가
# #{i: i * i for i in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# newitem = ['통밀빵','옥수수빵','크렌베리빵']
# b.update({ item: None for item in newitem})

# # 다음 항목에 대해 존재하면 출력 그렇지 않으면 예외 처리 진행 
# # 타겟 옥수수빵, 단팥빵
# target = ['옥수수빵','단팥빵']

# for key in target:
#     try:
#         print(key, b[key])
#     except KeyError: 
#         print("예외처리")
    
# # get 프레첼을조회 없으면 기본값 200으로 출ㄹ력
# if b.get("프레첼") is None : 
#     print(200)


# # items 를 사용해 전체 항목 출력 
# print(b.items)
# # 조건에 따른 가격조정 바게트, 치아바타는 50원 인상 , 스콘은 50원 이하 
# #치아 바타는 = 50원 인상 


# for key in b :
#     print(key)
#     if key == "바게트" or key== "치아바타": b[key] += 50
#     elif key =="스콘": b[key] -=50


# print(b)


# print("-"*40)
# print(" ---------- 61번 문제  ---------")
# print("-"*40)
# #다음 학생들의 정보를 이용 평균 점수 , 합격여부 출력 
# # 평균 60점 이상 합격 아님 불합격
# st = [
#     ['김현희',80,90,75,60,55],
#     ['강윤지',60,70,85,75,65],
#     ['윤지희',55,60,45,72,60],
#     ['한현민',95,80,90,90,85],
# ]

# total = 0 

# for x in st:
#     for y in range(1,len(x)):
#         total = total + x[y]
    
#     avg =total/len(x)    
    
#     if avg >= 60 :
#         print("%s 합격 총점 : %d  , 평균 %0.2f"%(x,total,avg) )
#     else:
#         print("%s 불합격 총점 : %d  , 평균 %0.2f"%(x,total,avg) )
        
#     total=0
#     avg = 0



# print("-"*40)
# print(" ---------- 70번 문제  ---------")
# print("-"*40)
# # list comprehension을 활용한 문제
# # 평균 이상 점수를 받은 학생 수 출력하기
# scores = [55, 80, 92, 45, 68, 88]  # 평균 이상이면 '우수'
# to = sum(scores)
# avg = to/len(scores)
# print(scores)
# print(" 평 균 점수 : %0.2f "% avg )
# [print("우수") for i in scores if i >= avg ]  


# # for t in scores:
# #     if t >= avg:
# #         print("우수")
# #     else:
# #         print("미흡")
    
# print("-"*40)

# # 나이가 18세 이상인 사람만 추출하여 몇 명인지 출력
# ages = [12, 17, 18, 20, 35, 15]
# c =0
# c = sum(1 for a in ages if a >= 18)
# # for a in ages:
# #     if a >= 18:
# #         c+=1
# print(" 18세 이상인 사람의 수 : %d "% c)
# print("-"*40)
# # 양수만 골라서 개수 출력하기
# numbers = [-5, 3, 0, 7, -2, 10, -8]
# c=0
# print("양수의 갯수 : %d " %sum( 1 for n in numbers if n>0 ))
# print("-"*40)
# # for a in numbers:
# #     if a > 0:
# #         c+=1

# # print ("양수의 갯수 : %d " % c)
# print("-"*40)
# # 짝수만 골라서 출력 및 개수 표시
# data = [1, 4, 7, 10, 13, 16]
# print ( " 짝수만 골라서 출력 및 개수 표시 %d  " % sum (1 for d in data if d%2==0 ))

 
# # 이름 리스트에서 3글자 이상인 이름만 추출
# names = ["유나", "철수", "민지", "Tom", "Ann", "Jennifer"]
# name = [n for n in names if len(n)>=3 ]
# print(name)




print("-"*40)
print("-" * 17 + f" {77}번 " + "-" * 17)
print("-"*40)

n = [ '바나나','사과','오렌지']
qty = [10,20,30]

nq = dict(zip(n,qty))
print(nq)
print("-"*40)

str1 = 'tqs'
str2= 'rtr'
str3 = dict(zip(str1,str2))
print(str3)
print("-"*40)




# 정수 2개 입력 -> 두수를 포함하고 사이의 모든 수를덧셈하는 프로그램을 만들어라 
# 앞자리 수가 뒷수보다 큰 경우 swap 을 이용해 두 변수의 값을 바꿔라 
#예시 3, 5 입력 = 3+ 4+ 5 
# 7,4 = 7+6+5+4 
# print("-"*40)
# print("-" * 17 + f" {74}번 " + "-" * 17)
# print("-"*40)

# a = int(input("1 수 입력 : "))
# b = int(input("2 수 입력 : "))
# if a > b : 
#     a,b = b,a
# t=0
# for c in range(a,b+1):
#     t+=c
# print(f"첫번째수{a}~ 두번째수 {b} 까지의 합은 {t}")

#다음 리스트의 요소 중에서 최소 값, 최대 값, 평균값을 요소로 하는 신규 튜플 생성 
#mylist=[10,20,30,40]
# print("-"*40)
# print("-" * 17 + f" {76}번 " + "-" * 17)
# print("-"*40)
# mylist=[10,20,30,40]
# m = min(mylist)
# am= max(mylist)
# ag=sum(mylist)/len(mylist)
# s = (m,am,ag)
# print(f"최소 값: {min(mylist)}, 최대값 : {max(mylist)} , 평균 값{ sum(mylist)/len(mylist) }")
# print(s)



#다음 리스트 이용 
# human = ['김철수', '홍길동', '박영희']
#jumsu =[50,60,70]
# print("-"*40)
# print("-" * 17 + f" {76}번 " + "-" * 17)
# print("-"*40)
# human = ['김철수', '홍길동', '박영희']
# jumsu =[50,60,70]

# mylist = list( zip(human,jumsu))
# print(mylist)
# mydict = dict(mylist)
# print(mydict)
# mydict=  sorted(dict(mylist))
# print(mydict)