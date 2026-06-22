#추상 클래스
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass #구현은 자식 클래스에서 반드시 해야함
class Dog(Animal):
    def speak(self):
        return "멍멍"
class Cat(Animal):
    def speak(self):
        return "야옹"

#객체 생성
dog =Dog()
print(dog.speak())
cat = Cat()
print(cat.speak())