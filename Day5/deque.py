from collections import deque
num=[1,2,3,4]
num=deque(num)
num.pop()#it will remove only last val
print(num)
num.popleft()#In deque we use poleft to remove left in which we can't do in list
print(num)