#finding sum of fib series
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
n=6
print(fib(n))