import time 
import sys 
sys.setrecursionlimit(1000000000)
def sumRecur(num): 
    if num == 1:
        return num
    else:
        return num+sumRecur(num-1)
    
    
if __name__ == '__main__':
    start = time.time()
    print(sumRecur(100000000))
    
    end = time.time()
    print(f'time taken by {sumRecur.__name__} fun : {end - start}')
    

# sumR(1)
# 2 + sumR(2-1)
# 3 + SumR(3-1)
# 4 + SumR(4-1)
