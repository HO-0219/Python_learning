#메타 클래스 

#메타 크래스 정의
class MyMeta(type):
    def __new__(cls,name,bases,class_dict):
        print(f"클래스{name}이 생성됨!")
        return super().__new__(cls,name,bases,class_dict)
#메타 클래스를 적용한 클래스
class MyClass(metaclass=MyMeta):
    pass

        