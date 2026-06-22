""" 리스트 컴프리 헨션"""
# 리스트 컴프리헨션은 리스트를 만드는 간결한 방법이다.
# 리스트 컴프리헨션은 대괄호([]) 안에 for 문을 포함한다.
# 기존 방식
"""
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

# 리스 컴프리헨션
ssquares = [i**3 for i in range(10)]
print(ssquares)

# 조건을 추가한 리스트 생성 
even_numbers=[]
for x in range(10):
    if x % 2 == 0: # 2로 나누어 떨어지는 수만 추가
        even_numbers.append(x)
print(even_numbers)

even_numbers = [x for x in range(10) if x % 3 == 0] # 3으로 나누어 떨어지는 수만 추가 
print(even_numbers)

# 중첩 FOR문 리스트 컴프리헨션
pairs = []
for x in range(10):
    for y in range(10):
        pairs.append((x,y))
print(pairs)    

print("=====================================")
#컴프리헨션 사용
pairs = [(x,y) for x in range(10) for y in range(10)]
print(pairs)
"""

"""Test """
#TEST1. 1부터 20까지의 숫자 중 3의 배수만 리스트로 생성해라.
#TEST2. 1부터 100까지 숫자 중에서 짝수인 숫자의 제곱을 리스트로 만들어라.
#TEST3. 문자열 리스트 ["apple", "banana", "cherry"]에서 길이가 5 이상인 단어만 필터링해서 새 리스트를 만들어라.
#TEST4. 두 개의 리스트 [1, 2, 3], [4, 5, 6]를 이용하여 모든 조합을 생성하는 리스트를 만들어라.

#TEST1
three_multiple = [x for x in range(1,21) if x % 3 == 0]
print(three_multiple)

#TEST2
even_square = [x**2 for x in range(1,101) if x % 2 == 0]
print(even_square)

#TEST3
words = ["apple", "banana", "cherry"]
five_words = [word for word in words if len(word) >= 5]
print(five_words)
#TEST4
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combination = [(x,y) for x in list1 for y in list2]
print(combination)

print("-==============")
# 내가 해보는 문제 
lista= [1,2,3,4,5]
listb = [5,4,3,2,1]
makelist =[(x,y) for x in lista for y in listb]
print(makelist)