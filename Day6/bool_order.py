arr=[1,1,0,1,1,0,0]
s1=[]
s2=[]
for i in arr:
    if i==0:
        print(i)
        s1.append(i)
    else:
        print(i)
        s2.append(i)
print(s1.extend(s2))
print(s1)

#2nd method using only one list but it won't work for another values
res=[]
for i in arr:
    if i==0:
        res.insert(i,0)
    else:
        res.append(i)
print(res)