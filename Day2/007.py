#예외 처리 
# 예외란 프로그램 실행중 오류가 발생하면 프로그램이 중단되는 문제를 방지하기 위해 사용
# 예외 처리는 try, except, finally 블록을 사용하여 처리
# try 블록에서 예외가 발생하면 except 블록이 실행
# finally 블록은 예외 발생 여부에 상관없이 항상 실행
# except 블록은 여러 개 사용할 수 있으며, 각 예외에 따라 다른 처리를 할 수 있음
# 예외는 Exception 클래스를 상속받은 클래스로 사용할 수 있음
# raise 키워드로 예외를 발생시킬 수 있음
# assert 키워드로 조건을 검사하고 예외를 발생시킬 수 있음
# 예외 처리는 함수를 사용할 때도 가능
# 함수에서 예외가 발생하면 호출한 곳으로 예외를 전달
# 호출한 곳에서 예외를 처리하지 않으면 다시 상위로 전달 
# 기본 try- excepy 문법
#try: 
#    실행할 코드 
#except 예외 as 변수: 
#    예외 처리 코드
# finally 블록은 생략 가능
try:
    a = 10 / 0  # 0으로 나누는 오류 발생
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
# 0으로 나눌 수 없습니다!
# 여러 예외 처리
try:
    num = int(input("숫자를 입력하세요: "))
    print(10 / num)  # 0을 입력하면 ZeroDivisionError 발생
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except ValueError:
    print("숫자를 입력하세요!")
# 예외 메시지 확인 
try:
    x = int("hello")  # ValueError 발생
except ValueError as e:
    print(f"예외 발생: {e}")
# 예외 발생: invalid literal for int() with base 10: 'hello'
# finally 블록 예외 방생 여부와 관계 없이 실행 
try:
    f = open("test.txt", "r")  # 파일 열기
    data = f.read()
except FileNotFoundError:
    print("파일이 존재하지 않습니다!")
finally:
    print("예외 처리 완료!")  # 항상 실행됨
# 예외 처리 완료!
# else 문 예외 방생하지 않았을때 실행 
try:
    num = int(input("숫자 입력: "))  
    result = 10 / num
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except ValueError:
    print("숫자를 입력하세요!")
else:
    print(f"결과: {result}")  # 예외가 발생하지 않으면 실행됨
# 결과: 2.5