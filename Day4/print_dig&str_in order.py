s='a1234d'
s1=''
s2=''
for c in s:
    if c.isdigit():
        s1+=c
    else :
        s2+=c
        
print(s1+s2)