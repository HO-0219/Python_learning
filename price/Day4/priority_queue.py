#우선순위 큐 (Priority Queue) 힙 큐heapq
import heapq

queue = []

heapq.heappush(queue, 3)
heapq.heappush(queue, 1)
heapq.heappush(queue, 4)
heapq.heappush(queue, 2)

print(heapq.heappop(queue)) #1 가장 작은 값이 우선
# 해당 코드는 queue 리스트에 3,1,2,4,2를 차례대로 추가하는 예시 코드입니다.

heap =[3,1,2,4,2]
heapq.heapify(heap)
print(heapq.heappop(heap)) #1
#해당 코드는 heapify 함수를 통해 즉각적으로 힙 자료형으로 변환할 수 있다.

#힙 원소 삭제 
result = heapq.heappop(heap)
print(result) #1
print(heap) #[2, 2, 4, 3]
#해당 코드는 힙에서 원소를 삭제하는 코드입니다.

#힙에서 가장 작은 원소인 1이 결과로 리턴되었고 힙에서 제거 됨을 볼 수 있다 
# 원소 삭제를 하지 않고 가져오고 싶다면 [n]을 통해 접근하면 된다.
result2 = heap[0]
print(result2) #2
print(heap) #[2, 2, 4, 3]
#해당 코드는 힙에서 원소를 삭제하지 않고 가져오는 코드입니다.

#최대 힙
#최대 힙을 구현하려면 부호를 바꾸어서 넣고 빼낼 때 다시 부호를 바꾸어주면 된다.
heap_items =[13,5,1,2,5]
max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))

print(max_heap) #[(-13, 13), (-5, 5), (-1, 1), (-2, 2), (-5, 5)]
#해당 코드는 최대 힙을 구현하는 코드입니다.
#heap push 함수를 통해 item을 힙에 추가 할대 (-item,item)의 튜플형태로 넣은것을 확인할 수 있음
# 그 결과로 heappop을 사용하게 되면 최대값이 반환될 수 있으며 이때 실제 원소 값은 튜블의 두번째 자리에 저장되어 있음으로 [1]인덱싱을 통해 접근하면 된다
max_item= heapq.heappop(max_heap)[1]
print(max_item) #13
#해당 코드는 최대 힙에서 원소를 빼내는 코드입니다.
print("========================")
#Test 주어진 리스트의 모든 값이 T 이상이 될때 까지 최소값 두개를 합치기


def my_heap_example(T,L):
    heapq.heapify(L)
    result = 0
    while len(L) >= 2:
        min_1 = heapq.heappop(L)
        if min_1 >= T:
            return result
        else:
            min_2 = heapq.heappop(L)
            result += 1
            heapq.heappush(L,min_1+min_2)
            print(f"step{result}: {min_1},{min_2}")
        
    if L[0] >= T:
        print(f"result: {result} {L}")
        return result
    else:
        print(f"result: {result} {L}")
        return -1
T = 7
L = [3,5,2,7,9,1,2]
retunl =my_heap_example(T,L)
print(retunl)
#해당 코드는 주어진 리스트의 모든 값이 T 이상이 될때 까지 최소값 두개를 합치는 코드입니다.
#1,2,2,3,5,7,9
# step1 : 1+2 = 3 # 1,2가 합쳐지게 되어 2,3,3,5,7,9
# step2 : 2+3 = 5 # 2와 3이 합쳐지게 되어 3,5,5,7,9
# step3 : 3+5 = 8 # 3과 5가 합쳐지게 되어 5,7,8,9
# step4 : 5+ 7 = 12 # 5와 7이 합쳐지게 되어 8,9,12

