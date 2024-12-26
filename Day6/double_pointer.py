#DoublePointer
arr=list(map(int,input().split(",")))
k=int(input())
#arr=[1,2,3,4,5]#array should be sorted
#k=6
count=0
f=0
l=len(arr)-1
while f<l:
    if arr[f]+arr[l]==k:
        count+=1
        f+=1
        l-=1
    elif arr[f]+arr[l]<k:
        f+=1
    else:
        l-=1
print(count)
