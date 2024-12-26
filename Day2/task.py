#n=500  2,4,8     find the combination of those numbers each with equal no of times
'''requirements
1)2 functions
2)for loop
3)if condition'''
def check(num):
    num=str(num)

    twos=num.count('2')
    fours=num.count('4')
    eights=num.count('8')


    return twos==fours==eights and twos>0


def increment(N):
    count=0
    for num in range(1,N+1):
        if check(num):
            print(num)
            count+=1
    return count

N=int(input())
print(increment(N))