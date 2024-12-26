arr=[1,3,6,2,5,3,7,5,1]
d={}
for key in arr:
#calculating frequency of elements
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
print(d)
for num,count in d.items():
    if count==1:#checking unique ele
        print(num)
    