# 퀵정렬
def quick_sort(arr):
    if len(arr) <= 1: # 리스트 크기가 1이ㅏ면 정렬할 이유가 없음
        return arr
    
    pivot = arr[len(arr)//2] # 중간 값을 피벗으로 선택
    left = [x for x in arr if x< pivot] # 피벗보다 작은 값
    middle = [x for x in arr if x == pivot] # 피벗이랑 같은값
    rigth = [x for x in arr if x > pivot] # 피번보다 큰값

    return quick_sort(left) + middle + quick_sort(rigth)

arr = [64, 34, 25, 12 ,22, 11, 90]
sorted_arr = quick_sort(arr)
print(sorted_arr)