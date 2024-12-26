n=2397
n=str(n)
m=3
add=0
mul=0

for i in n:
    if int(i)%2==0:
        add=int(i)+m
        print(add)
    else:
        mul=int(i)*m
        print(mul)

