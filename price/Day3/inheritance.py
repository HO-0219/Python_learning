#상속 
#부모 클래스
class Animal:
    def __init__(self,name):
        self.name = name

    def move(self):
        return "움직인다"

#자식 클래스
class Dog(Animal):
    def speak(self):
        return "멍멍"
    #def move(self):   
        #return "걷는다"
#자식 클래스
class Cat(Animal):
    def speak(self):
        return "야옹"
    #def move(self):   
        #return "걷는다"

#객체 생성
# dog = Dog("멍멍이
# print(dog.name)
# print(dog.move())
animals = [Dog("멍멍이"), Cat("나비")]
for animal in animals:
    print(animal.name)
    print(animal.move())
    print(animal.speak())
#다형성
#부모 클래스 타입으로 자식 클래스 객체를 다루기
# dog = Dog("멍멍이")
# cat = Cat("나비")
# animals = [dog, cat]
