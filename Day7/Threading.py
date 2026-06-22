#스레딩 
import threading
import time

def task(name, sec):
    print(f"{name} 시작 ....")
    time.sleep(sec)
    print(f"{name} 완료!")

t1 = threading.Thread(target=task,args=("작업 1",4))
t2 = threading.Thread(target=task,args=("작업 2",2))
t1.start()
t2.start()

t1.join()
t2.join()

