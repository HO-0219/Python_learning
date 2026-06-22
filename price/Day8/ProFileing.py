# 프로파일링 

import cProfile

def slow_function():
    sum([i**2 for i in range(1000)])
    
cProfile.run('slow_function()')

