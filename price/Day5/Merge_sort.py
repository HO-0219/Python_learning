# 병합 정렬 코드 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid]) # 왼쪽 절반 정렬
    right = merge_sort(arr[mid:]) # 오른쪽 반 정렬

    return merge(left,right)

def merge(left, rigth):
    result = []
    i = j = 0
    while i < len(left) and j < len(rigth):
        if left[i] < rigth[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(rigth[j])
            j+=1
    result.extend(left[i:])
    result.extend(rigth[j:])
    return result

arr = [64,34,25,25,21,22,11,90]
sorted_arr = merge_sort(arr)
print(sorted_arr)

