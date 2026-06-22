#람다 함수 
# 람다 함수란 이름없이 간단한 연산을 수행하는 익명의 함수 이며 한줄짜리 함수를 만들때 사용함

#1 기본적인 람다 함수
"""
def add(x,y):
    return x+y
print(add(4,10))

print(" 람다 함수를 사용하여 변환")

add_lamda =lambda x,y:x+y
print(add_lamda(4,10))
"""
"""
#2 내장 함수와 함께 사용 map, fillter, sorted
numbers =[1,2,3,4,5]

#일반 함수시 
def square(x):
    return x*2
result = list(map(square,numbers)) #리스트의 요소를 지정된 함수로 처리
print(result)
# 람다 함수 사용
result = list(map(lambda x: x**2, numbers)) #map 리스트의 요소를 지정된 함수로 처리
print(result)  # [1, 4, 9, 16, 25]

#filter 함수
numbers =[1,2,3,4,5,6,7,8,9,10]
#짝수
even_number = list(filter(lambda x: x%2==0, numbers))
print(even_number) # [2, 4, 6, 8, 10]

#sorted 함수
words = ['apple','banana','cherry','dragon','elephant']
#길이 기준으로 정렬 
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) #['apple', 'banana', 'cherry', 'dragon', 'elephant']

"""
# TEST 
# map을 사용하여 리스트 3,6,9,12의 모든 숫자를 3배한 리스트를 만들어라 
# filter을 사용하여 리스트 10,15,20,25,30에서 15보다 큰숫자만 필터링해라
# sorted를 사용하여 문자열 리스트를 문자열 길이로 정렬해라
# 리스트 1,2 3,4  5,0 2,4 의 두번째 요소기준으로 정렬하라 

#test 01 
list1 = list(map(lambda x: x*3, [3,6,9,12]))
print(list1)

#test 02
list2 = list(filter(lambda x: x>15, [10,15,20,25,30]))
print(list2)

#test 03
list3 = sorted(['apple','banana','cherry','dragon','elephant'], key=lambda x: len(x))
print(list3)
# test 04
list4 = sorted([(1,2),(3,4),(5,0),(2,4)], key=lambda x: x[1])
print(list4)