#이진 탐색 코드 

# 재귀 이진 탐색 코드 
def binary_search(arr, target, left, right):
    if left > right:
        return -1 #못찾음 -1
    mid = (left + right) //2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,right)
    else:
        return binary_search(arr,target,left,mid-1)

arr =[11,22,33,44,55,66,90]
target = 33
result = binary_search(arr,target,0,len(arr)-1)
if result != -1:
    print(arr[result], result)
else:
    print( "not found")

# 반복 이진 탐색 코드 
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 찾으면 인덱스 반환
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽 탐색
        else:
            right = mid - 1  # 왼쪽 탐색

    return -1  # 못 찾으면 -1 반환

arr = [11, 22, 25, 34, 64, 90]
target = 33
result = binary_search_iterative(arr, target)

if result != -1:
    print(arr[result],result)
else:
    print(" not found")
