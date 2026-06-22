#HTTP 통신 예제 

#Get 요청 예제 
import requests

response = requests.get("https://주소/")
data = response.json() # json 응답을 파이썬 딕셔너리로 변환

print(data)

#POST 요청 예제
url = "http://주소 /post"
data = {"title" : "text", "body" :"context", "userId":1}
response = requests.post(url,json=data)
print(response.json())
