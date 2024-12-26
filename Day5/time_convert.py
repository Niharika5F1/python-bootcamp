time='24:60:60'

time=time.split(':')
#print(time)
hrs=time[0]
min=time[1]
sec=time[2]
#print(hrs,min,sec)
if int(hrs)>=24:
    hrs=int(hrs)-24
else:
    hrs=int(hrs)-12

#print(hrs,min,sec)
if int(min)>59:
    hrs=int(hrs)+1
    min=int(min)-60
#print(hrs,min,sec)
if int(sec)>59:
    min=int(min)+1
    sec=int(sec)-60
print(str(hrs)+':'+str(min)+':'+str(sec))


