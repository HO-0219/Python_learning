#파이썬에서 스택 구조 
stack = []

#push(삽입)
stack.append(1)
stack.append(2)
stack.append(3)

#pop(삭제)
print(stack.pop()) #3

#비어있는 경우 에러 발생

#peek(가장 위에 있는 값 확인)
print(stack[-1]) #2

#is _empty(비어있는지 확인)
print(len(stack)== 0) #False