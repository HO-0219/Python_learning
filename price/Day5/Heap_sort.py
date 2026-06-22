#힙 정렬
def heapify(arr, n, i):
    largest = i  # 루트 노드
    left = 2 * i + 1  # 왼쪽 자식
    right = 2 * i + 2  # 오른쪽 자식

    # 왼쪽 자식이 루트보다 크면 교체
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 가장 크다면 교체
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 변경되었다면 스왑하고 재귀적으로 정렬
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 최대 힙 생성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 힙에서 꺼내 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최대값(루트)과 마지막 노드 교환
        heapify(arr, i, 0)  # 힙 다시 정렬

arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print(arr)
