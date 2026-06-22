#클래스 정의 
class Car:
    def __init__(self, brand, model): # 생성자
        self.brand = brand #instance variable
        self.model = model #instance variable

    def show_info(self):
        print(f"자동차 브랜드:{self.brand}, 모델:{self.model}")

#객체 생성
my_car = Car("Toyota", "Prius")
my_car.show_info()
