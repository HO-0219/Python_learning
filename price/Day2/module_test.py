#모듈 사용하기
"""
import module_008

print(module_008.add(10, 4))
print(module_008.multiply(10, 4))
"""
#모듈에서 특정 함수만 가져오기 
from module_008 import add
print(add(10, 4))