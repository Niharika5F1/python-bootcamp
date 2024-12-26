n=input()
l=len(n)
k=int(input())
res=[]
for i in range(l-k+1):
    subs=n[i:i+k]
    res.append(subs)
    if len(n)-1:
        
for i in res:
    print(i)


    
    