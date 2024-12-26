s=7
t=11
a=3
b=15
c1=0
c2=0

apples=[6,5,-4]
oranges=[9,8,-4]
acount=0
ocount=0
#using range function
for i in apples:
    if a+i in range(s,t+1):
        acount+=1

for i in oranges:
    if b+i in range(s,t+1):
        ocount+=1

print(acount+ocount)

#using <= and >= operators
'''for i in apples:
    if s<= a+i <=t:
        c1+=1
print(c1)
        
for i in oranges:
    if s<= b+i <=t:
        c2+=1
        print(c2)

print(c1+c2)'''



    
