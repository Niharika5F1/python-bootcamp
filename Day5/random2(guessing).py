import random
ran=random.randint(1,10)
chances=1
'''while chances<=3:
    guess=int(input())
    if guess==ran:
        print('congrats')
        break
    else:
        chances+=1
        continue
if chances>3:
    print('failed to try next time')'''
# if we want true infinately then in while give true
while True:
    guess=int(input())
    if guess==ran:
        print('congrats')
        
    else:
        continue
    print('failed')
