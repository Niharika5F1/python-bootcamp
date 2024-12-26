'''Alice and Bob has values [10,3,6] and [12,3,4] 
a,b=0,0
a=1 and b=1'''
a=list(map(int,input().split(",")))
b=list(map(int,input().split(",")))
alice_points=0
bob_points=0
for i in range(len(a)):
        if a[i]>b[i]:
            alice_points+=1
        elif a[i]<b[i]:
            bob_points+=1
        else:
            alice_points+=1
            bob_points+=1
if alice_points>bob_points:
    print("alice wins")
elif alice_points<bob_points:
    print("bob wins")
else:
     print("both wins") 



            

