#버블 정렬 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False # 최적화 이미 정렬이 된경우
        for j in range(n-i-1):
            if arr[j] > arr[j+1]: # 인접한 두 원소를 비교
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap
                swapped = True 
        if not swapped:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)