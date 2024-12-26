s='abcdz'
s1=''
for c in s:
    #print(ord(c))  #it gives ascii values of alphabets
    #print(chr(ord(c)+1)) #chr is for printing character
    if ord(c)>=97 and ord(c)<122:
        s1+=chr(ord(c)+1)
    else:
        s1+=chr(ord(c)-25)

print(s1)

