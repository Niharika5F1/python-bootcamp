stu=(101,'niha','cse','hyd')
#we cannot directly make changes to tuple instead convert it into list and make changes
stu=list(stu)
stu[2]='ece'
print(stu)
stu.append('sspet')#for adding
print(stu)
stu.pop(2)
print(stu)
