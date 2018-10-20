import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(10):
    start = time.time()
    val = fib(35)
    end = time.time()  
    print(str(end - start))
