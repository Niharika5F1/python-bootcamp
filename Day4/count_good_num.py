'''GOOD NUMBERS'''
import math
arr=[35,9,1]
count=0
for ele in arr: 
    low=1
    high=math.ceil(ele**0.3)
    while low<high:
        res=low**3+high**3
        print(ele)
        if res==ele:
            count+=1
        low+=1
        
print('the count is:',count)