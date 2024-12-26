mobile=['iphone','samsung','vivo','oppo','moto']
mobile.append('oneplus')
print(mobile)
mobile.remove('vivo')
print(mobile)
mobile.pop(1)#removes ele
print(mobile)
mobile[1]='redmi'#updates at a position
print(mobile)
print(mobile[True])#returns 1th index value if false returns 0th value from the list
count=0
for ele in mobile:#printing the ele of list
    print(count,ele)
    count+=1
for i in range(0,len(mobile)):#even values
    if i%2==0:
        print(mobile[i])
for i in range(0,len(mobile)):#even values
    rev=mobile[i]
    print(rev[::-1])#we can only rev of words not cmplt list ele
#[1,2,3,4,5],k=4  ->o/p:-[4,5,1,2,3]
arr=[1,2,3,4,5]
k=4
first=arr[k-1:]#prints values before the k
second=arr[:k-1]#prints values after the 
print(first+second)

       

