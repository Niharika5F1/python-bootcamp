menu={
    'juice':10,
    'shake':24,
    'biryani':50
}
print(menu)
menu['curry']=60#inserting the new value
print(menu)
menu['shake']=20#updating the value
print(menu)
menu.pop('juice')#to remove a value
print(menu)
print(menu.keys())#to print keys
menu.items()
print(menu.values())#the values of keys


