#멀티 프로세싱 코드

# import multiprocessing
# import time

# def task(name, sec):
#     print(f"{name} 시작...")
#     time.sleep(sec)
#     print(f"{name} 완료!")

# p1 = multiprocessing.Process(target=task, args=("작업 1", 3))
# p2 = multiprocessing.Process(target=task, args=("작업 2", 2))

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# 위의 코드들은 맥 환경에서 spawn 방식이 기본으로 설정되어 문제가 있음 
import multiprocessing
import time

def task(name,sec):
    print(f"{name} 실행! ")
    time.sleep(sec)
    print(f"{name} 완료!")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task,args=("작업1",4))
    p2 = multiprocessing.Process(target=task,args=("작업2",3))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
