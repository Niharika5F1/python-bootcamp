candles=[3,7,1,5,4]
#print(candles.count(max(candles)))  with max()
max=0
count=0
for i in candles:
    if i>max:
        max=i
for  i in candles:
    if max==i:
        count+=1
print(count)
