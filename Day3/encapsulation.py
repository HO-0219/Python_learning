#캡슐화 
class Person:
    def __init__(self,name,age):
        self.name = name #public 변수
        self._job ="개발자" #protected  변수
        self.__age = age #private 변수
    def show_info(self):
        print(f"이름:{self.name}, 직업:{self._job}, 나이:{self.__age}")

#객체 생성
person = Person("홍길동",20)
print(person.name) #접근 가능
print(person._job) #접근 가능 하지만 권장하진 않음
#print(person.__age) #접근 불가능
#private 변수 접근 우회방법
print(person._Person__age)