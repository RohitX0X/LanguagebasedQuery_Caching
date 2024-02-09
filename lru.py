from functools import lru_cache 
import time 
@lru_cache(maxsize = 128) 
def fib_with_cache(n): 
    if n < 2: 
        return n 
    return fib_with_cache(n-1) + fib_with_cache(n-2) 
      
begin = time.time() 
fib_with_cache(40) 
end = time.time() 
  
print("Time taken to execute the function with lru_cache is", end-begin) 