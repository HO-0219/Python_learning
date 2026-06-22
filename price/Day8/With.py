#컨텍스트 매니저 with문

# 앞서 하게 된파일 입출력 
with open("./test2.txt","w") as file:
    file.write("hellow, Python!!!!!! \n")

# 직접 컨텍스트 매니저 만들기
class MyContextManager:
    def __enter__(self):
        print("리소스 열기!!!!")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print("리소스 닫기")

with MyContextManager():
    print("작업 수행 중~! ")