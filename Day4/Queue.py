#큐 Queue

from collections import deque
queue = deque()

#enqueue(삽입)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

#dequeue(삭제)
print(queue.popleft()) #1

#fornt(가장 앞에 있는 값 확인)
print(queue[0]) #2

#is_empty(비어있는지 확인)
print(len(queue) == 0) #False
#큐는 선입선출 구조이다.
