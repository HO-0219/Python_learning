
def insertion_sort(arr):
    n =len(arr)
    for i in range(1,n): # 두번째 요소부터 시작
        key = arr[i] # 현재 삽입할 값
        j = i-1 # 이전 요소를 가르키는 인덱스
        
        while j>= 0 and arr[j] >key:
            arr[j+1] = arr[j]
            j -=1

        arr[j+1]= key

arr  = [64,34,26,12,22,11,90]
insertion_sort(arr)
print(arr)


