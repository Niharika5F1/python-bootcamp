#sum of digit until it became single digit
def sum(n):
    val=0
    while n>0:
        rem=n%10
        val+=rem
        n=n//10
    return val

def single(n):
        while n>9:
            n=sum(n)
        return n

num=789
print(single(num))

      
