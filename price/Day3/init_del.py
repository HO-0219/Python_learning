#생성자와 소멸자

class Example:
    def __init__(self, name):
        self.name = name
        print(f"생성자 호출, 이름:{self.name}")
        
    def __del__(self):
        print(f"소멸자 호출, 이름:{self.name}")

#객체 생성 및 삭제
ex = Example("instance")
#del ex