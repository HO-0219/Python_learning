#해시 테이블 구현
#Dictionary를 이용하여 해시 테이블 구현
#해시 테이블은 키와 값으로 구성된 데이터를 저장하는 자료구조

hash_table = {}
#해시 테이블에 데이터 삽입
hash_table["name"] = "alice"
hash_table["age"] = 30

#해시 테이블에서 데이터 조회
print(hash_table["name"])

#해시 테이블에서 데이터 삭제
del hash_table["name"]

print(hash_table)
#해시 테이블은 데이터를 삽입, 조회, 삭제하는데 O(1)의 시간 복잡도를 가진다.

# 공간 복잡도 
car_data = {
    "자동차": {
        "기아": {
            2023: {
                "K5": {"색상": "흰색", "가격": "3000만원"},
                "쏘렌토": {"색상": "검정색", "가격": "4000만원"},
            }
        }
    }
}

# 검색 예시
category = "자동차"
brand = "기아"
year = 2023
model = "K5"

result = car_data.get(category, {}).get(brand, {}).get(year, {}).get(model)

if result:
    print(f"{category} {brand} {year}년 {model}: {result}")
else:
    print("검색 결과 없음")

print("+=================-==-=-=-=-=====")
# 시간 복잡도가 높음 
car_data = {}

# 데이터 저장 (복합 키 사용)
car_data[("자동차", "기아", 2023, "K5")] = {"색상": "흰색", "가격": "3000만원"}
car_data[("자동차", "기아", 2023, "쏘렌토")] = {"색상": "검정색", "가격": "4000만원"}

# 검색 예시
category = "자동차"
brand = "기아"
year = 2023
model = "K5"

key = (category, brand, year, model)
result = car_data.get(key)

if result:
    print(f"{category} {brand} {year}년 {model}: {result}")
else:
    print("검색 결과 없음")

# 특정 조건에 맞는 데이터 검색 (선형 검색 활용)
search_year = 2023
results = []
for k, v in car_data.items():
    if k[2] == search_year: # 튜플의 3번째 값이 생산년도
        results.append((k, v))

if results:
    print(f"{search_year}년 생산 차량:")
    for k, v in results:
        print(f"{k[0]} {k[1]} {k[3]}: {v}")
else:
    print(f"{search_year}년 생산 차량 없음")