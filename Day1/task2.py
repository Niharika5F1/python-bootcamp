#printing reverse of 2nd half in 1st place
def revdig(s):
    for i in s:
        rev=i[::-1]
    return rev

def num(n):
  mid=0
  while n>0:
     rem=n%10
     count+=rem
     if count==len(n):
         mid=len(count)//2
         first_half=count[:mid]
         second_half=count[mid:]
         reverse(first_half,second_half)
         revdig(first_half)
     return first_half,second_half

n=145367
print(num(n))




