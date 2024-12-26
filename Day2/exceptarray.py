try:
    arr=[1,7,8,12,36]
    print(arr[0])
except IndexError:
    print('cannot access index error')
else:
    print('no exception occured')
finally:#whether the exception occurs or not it will execute finally
    print('finally wed is the last day')