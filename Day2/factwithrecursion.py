def fact(n):#recursive function
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input())
print(fact(n))